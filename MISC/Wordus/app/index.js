const express = require('express');
const https =  require('https')
const http = require('http')
const { Server } = require("socket.io");
const uuid4 = require('uuid4');
const fs = require('fs')
const path = require('path')

const app = express();

/*const server = https.createServer({
    key: fs.readFileSync(path.join(__dirname, 'cert', 'wordus.xyz.key.pem')),
    cert: fs.readFileSync(path.join(__dirname, 'cert', 'wordus.xyz.cert.pem'))
},app);*/

const server = http.createServer(app)


const io = new Server(server);

const User = require('./js/classe/User');
const Room = require('./js/classe/Room');
const Game = require('./js/classe/Game');

const RoomFactory = require('./js/factories/RoomFactory');
const GameFactory = require('./js/factories/GameFactory');
const GameStats = require("./js/classe/GameStats");
const RF = new RoomFactory();
const GF = new GameFactory();

require('events').EventEmitter.defaultMaxListeners = 0

const {
    roomCode,
    codeExists,
    genWords,
    genSingleWord
} = require('./js/functions');

global.rooms = {}
global.users = {}

app.use(express.static(__dirname+'/'));

/**
 * Page d'acceuil du site + page pour créer un room
 */
app.get('/', (req, res) => {
    res.sendFile(__dirname + '/views/index.html');
});

/**
 * Page de jeu principale
 */
app.get('/game', (req, res) => {
    res.sendFile(__dirname + '/views/game.html');
});

/**
 * Page pour rejoindre une room
 */
app.get('/join', (req, res) => {
    res.sendFile(__dirname + '/views/join.html');
});

app.get('/sitemap.xml', (req, res) => {
    res.sendFile(__dirname + '/sitemap.xml')
})

io.on('connection', socket => {

    ///////////// PAGE INDEX/HOST ROOM /////////////

    /**
     * Demande d'un client pour créer une nouvelle room
     */
    socket.on('host_room', (preferences, name, color, avatar) => {
        const uuid = uuid4();
        const owner = new User(uuid, name, color, avatar);

        let code = roomCode();
        if (codeExists(code)) {
            code = roomCode();
        }

        const room = new Room(code, owner, preferences);
        const game = new Game(code, preferences.gameDuration, preferences.wordAmount, preferences.lang);
        room.setGame(game)

        global.rooms[code] = room;
        global.users[uuid] = {socket, code}

        console.log(`New room - CODE : ${code}, owner : {uuid: ${uuid}, name: ${name}}, preferences : ${JSON.stringify(preferences)}`)

        socket.join(code);
        socket.emit('success_host_room', code, uuid);
    });

    ///////////// PAGE JOIN /////////////

    /**
     * Demande d'un client pour verifier l'existence d'une room
     */
    socket.on('exist_room', (code) => {
        /* Si la room n'existe pas */
        if (!global.rooms[code]) return socket.emit('no_room');

        /* Si il n'y a plus de place dans la room (> 6) */
        if (global.rooms[code].getNbUsers() >= 6) return socket.emit('no_place')

        /* On attribut la couleur en fonction du nombre de joueurs dans la room (par default le premier est jaune) */
        let color
        switch (global.rooms[code].getNbUsers()) {
            case 1:
                color = 'pink';
                break;
            case 2:
                color = 'purple';
                break;
            case 3:
                color = 'blue';
                break;
            case 4:
                color = 'green';
                break;
            case 5:
                color = 'brown';
                break;
        }

        socket.emit('room_exist', color);
    })

    /**
     * Demande du client pour créer un nouvel utilisateur
     */
    socket.on('create_user', (code, name, color, avatar) => {
        const uuid = uuid4();
        const newUser = new User(uuid, name, color, avatar);

        global.rooms[code].addUser(newUser);
        global.users[uuid] = {socket, code}

        socket.emit('created_user', code, uuid);
    });

    ///////////// PAGE GAME /////////////

    /**
     * Lorsqu'un client arrive sur la page /game de sa room
     */
    socket.on('join', (code, uuid) => {
        if (global.rooms[code] === undefined) return;

        const game = global.rooms[code].getGame();
        game.addUser(uuid);

        global.rooms[code].setGame(game)
        global.users[uuid] = {socket, code}

        socket.join(code);
        io.sockets.in(code).emit('new_join', global.rooms[code]);
    })

    /**
     * Start Game Event
     */
    socket.on('start_game', (code) => {
        if (global.rooms[code] === undefined) return;

        const game = global.rooms[code].getGame();

        genWords(game);

        // Start the game by changing the status
        game.startGame(io);
        console.log(code, 'Game Started')

        global.rooms[code].setGame(game)

        socket.join(code);
        io.sockets.in(code).emit('game_started', global.rooms[code])
    });

    /**
     * Input d'un client
     */
    socket.on('input', (code, word_input, letters, uuid) => {
        if (global.rooms[code] === undefined) return;

        //console.log(code, word_input, letters, uuid)

        const game = global.rooms[code].getGame()
        const user = global.rooms[code].getUsers()[uuid]
        const words = game.getWords()

        for (const key in words) {
            let w = words[key]

            if (w.include(word_input) && letters.length > 0) {
                w.addUser(uuid, user.getInfo().color)
            } else {
                w.removeUser(uuid)
            }
        }

        game.setWords(words);
        global.rooms[code].setGame(game)

        socket.join(code);
        io.sockets.in(code).emit('update_letter', global.rooms[code])
    });

    /**
     * Lorsque le client presse `ENTER` pour envoyer un mot
     */
    socket.on('press_enter', (code, word_input, letters, uuid) => {
        if (global.rooms[code] === undefined) return;

        const game = global.rooms[code].getGame()
        const user = global.rooms[code].getUsers()[uuid]
        const words = game.getWords()

        const verifyW = []
        let word_final

        for (const key in words) {
            if (words[key].equalWord(word_input)) {
                word_final = words[key]
                delete words[key]
                words[key] = genSingleWord(game, word_final)
                verifyW.push('o')
            } else {
                verifyW.push('x')
            }
        }

        let GS = game.getUserGameStats(uuid);
        switch (user.getCombos()) {
            case 0:
                GS.setMultiplier(1)
                break
            case 1:
                GS.setMultiplier(1.5)
                break
            case 2:
                GS.setMultiplier(2)
                break
            case 3:
                GS.setMultiplier(2.5)
                break
            default :
                GS.setMultiplier(3)
                break
        }

        let pts = Math.floor(letters.length/2)
        let signe = '-'
        if (verifyW.includes('o')) {
            pts = letters.length * GS.getMultiplier()
            signe = '+'
            user.addCombos();
            GS.addPoints(pts)
        } else {
            user.resetCombos()
            GS.removePoints(pts)
        }

        //console.log('combos', user.getCombos(), 'multiplier', GS.getMultiplier(),'score' , GS.getScore(), 'letters', letters.length, 'pts', pts, 'signe', signe)

        const win_info = {
            uuid: uuid,
            pts: pts,
            word: word_final !== undefined
                ? word_final
                : {word: word_input},
            sign: signe
        }

        game.setWords(words);

        global.rooms[code].setGame(game)
        socket.join(code);
        io.sockets.in(code).emit('word_finish', win_info, global.rooms[code])
    });

    /**
     * Lorsque l'owner de la game envoie une demande pour démarrer une nouvel partie
     */
    socket.on('restart_game', (code, t) => {
        if (global.rooms[code] === undefined) return;

        const game = global.rooms[code].getGame()
        game.setPreferences(t.gameDuration, t.wordAmount, t.lang)

        game.setWords([])
        game.setStatus(1)

        for (const uuid in game.getUsers()) {
            game.getUsers()[uuid] = new GameStats();
        }

        for (const uuid in global.rooms[code].getUsers()) {
            const u = global.rooms[code].getUsers()[uuid]
            u.resetCombos()
        }

        global.rooms[code].setGame(game)

        socket.join(code)
        io.sockets.in(code).emit('game_restarted', global.rooms[code])
    });

    /**
     * Demande du client pour récupérer une room à jours
     */
    /*socket.on('update_room', (code, room) => {
        const pre_room = global.rooms[code];
        const new_room = RF.getFromSocket(room);

        console.log(pre_room.users)

        pre_room.setPreferences(new_room.getPreferences());

        const pre_game = pre_room.getGame();
        const new_game = new_room.getGame();

        for (const key in new_game.getUsers()) {
            if (pre_game.hasOwnProperty(key)) return;
            pre_game.addUser(key, new_game.getUserGameStats(key));
        }

        console.log(pre_room.users)

        socket.join(code);
        io.sockets.in(code).emit('updated_room', global.rooms[code]);
    });*/

    /**
     * On client disconnect
     */
    socket.on('disconnect', (socket_t) => {

        if (socket.handshake.headers.referer.endsWith('/game')) {
            for (const uuid in global.users) {
                const user = global.users[uuid]
                if (user === undefined) return
                if (user.socket.id === socket.id) {
                    const userHasLeft = global.rooms[user.code].getUsers()[uuid]

                    if (global.rooms[user.code].getOwner().getUUID() === uuid) {
                        setTimeout(() => {
                            delete global.rooms[user.code]
                            socket.leave(user.code)
                        }, 40000)

                        socket.join(user.code)
                        return io.sockets.in(user.code).emit('owner_left', userHasLeft)
                    } else {
                        const game = global.rooms[user.code].getGame()

                        global.rooms[user.code].removeUser(uuid)
                        game.removeUser(uuid)

                        global.rooms[user.code].setGame(game)

                        socket.join(user.code)
                        return io.sockets.in(user.code).emit('user_left', global.rooms[user.code], userHasLeft)
                    }
                }
            }
        }
    })
});

server.listen(3000, () => {
    console.log('server running on port 3000')
});