const Game = require('../classe/Game');
const Word = require('../classe/Word')

const GameStatsFactory = require('./GameStatsFactory');
const GSF = new GameStatsFactory();

class GameFactory {
    getFromSocket = game => {
        const g = new Game(
            game.roomCode,
            game.duration,
            game.wordAmount,
            game.lang
        );

        g.setStatus(game.status)

        let words = []
        for (const word in game.words) {
            const w = new Word(game.words[word].word, game.words[word].position)

            Object.keys(game.words[word].users).forEach(uuid => {
                w.addUser(uuid, game.words[word].users[uuid])
            });

            words.push(w)
        }/*
        game.words.forEach(word => {
            const w = new Word(word.word, word.position)

            Object.keys(word.users).forEach(uuid => {
                w.addUser(uuid, word.users[uuid])
            });

            words.push(w)
        });*/
        g.setWords(words)

        g.setTimeLeft(game.timeleft)

        for (const k in game.users) {
            g.addUser(k, GSF.getFromSocket(game.users[k]));
        }
        return g;
    }
}

module.exports = GameFactory;