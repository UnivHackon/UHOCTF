const GameStats = require('./GameStats');

const Status = {
    WAITING: 1,
    PLAYING: 0,
    ENDED: -1
}

class Game {
    roomCode
    status
    words
    users
    duration
    endtime
    startTime
    timeleft
    wordAmount
    socket
    lang

    constructor(roomCode, duration, wordAmount, lang = 'fr') {
        this.roomCode = roomCode;
        this.status = Status.WAITING;
        this.words = {};

        this.duration =  duration;
        this.wordAmount = wordAmount;

        this.users = {}
        this.lang = lang
    }

    startGame = (io) => {
        this.status = Status.PLAYING;

        this.startTime = Date.now();
        this.endtime = this.startTime + (1000 *  this.duration)

        var interval = setInterval(() => {
            if (Date.now() - this.startTime > this.duration * 1000) {
                clearInterval(interval)
                this.status = Status.ENDED;
                return io.sockets.in(this.roomCode).emit('game_finish', this);
            }
            this.updateTimeLeft(io)
        }, 1000);
    }

    setWords = (words) => {
        if (words.length === 0) this.words = {}
        for (let i = 0; i < words.length; i++) {
            this.words[i] = words[i]
        }
    }

    getWords = () => {
        return this.words;
    }

    getUsers = () => {
        return this.users;
    }

    getNbPlayer = () => {
        return Object.keys(this.users).length;
    }

    getWordAmount = () => {
        return this.wordAmount;
    }

    getDuration = () => {
        return this.duration
    }

    getUserGameStats = (uuid) => {
        return this.users[uuid];
    }

    addUser = (uuid, gameStat = new GameStats()) => {
        this.users[uuid] = gameStat;
    }

    removeUser = (uuid) => {
        delete this.users[uuid];
    }

    setUsers = (users) => {
        this.users = users;
    }

    updateTimeLeft = (io) => {
        this.timeleft = this.endtime - Date.now()
        io.sockets.in(this.roomCode).emit('update_time', this.getTimeLeftFormated())
    }

    getTimeLeft = () => {
        return this.timeleft;
    }

    setTimeLeft = (timeleft) => {
        this.timeleft = timeleft
    }

    getTimeLeftFormated = () => {
        let seconds = Math.floor((this.timeleft / 1000) % 60);
        let minutes = Math.floor((this.timeleft / (1000 * 60)) % 60);

        minutes = (minutes < 10) ? "0" + minutes : minutes;
        seconds = (seconds < 10) ? "0" + seconds : seconds;

        if (this.timeleft < 1000) return `00:00`;

        return `${minutes}:${seconds}`
    }

    getDurationFormated = () => {
        let seconds = Math.floor(this.duration % 60);
        let minutes = Math.floor((this.duration - seconds) / 60);

        minutes = (minutes < 10) ? "0" + minutes : minutes;
        seconds = (seconds < 10) ? "0" + seconds : seconds;

        return `${minutes}:${seconds}`
    }

    getStatus = () => {
        switch (this.status) {
            case Status.WAITING:
                return 'WAITING';
            case Status.PLAYING:
                return 'PLAYING';
            case Status.ENDED:
                return 'ENDED';
        }
    }

    setStatus = (status) => {
        this.status = status;
    };

    getScoreBoard = () => {
        let sortable = [];
        for (const key in this.users) {
            const gameStat = this.getUserGameStats(key);
            sortable.push([this.users[key], gameStat.getScore()]);
        }

        sortable.sort((a,b) => {
            return b[1] - a[1];
        });

        return sortable
    }

    setPreferences = (newTime, newWords, newLang) => {
        this.duration = newTime;
        this.wordAmount = newWords;
        this.lang = newLang
    }

    getLang = () => {
        return this.lang
    }

    setLang = (lang) => {
        this.lang = lang
    }
}

module.exports = Game;