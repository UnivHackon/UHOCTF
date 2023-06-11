const GameStats = require('../classe/GameStats');

class GameStatsFactory {
    getFromSocket = gameStat => {
        const gs = new GameStats();
        gs.setScore(gameStat.score);
        gs.setMultiplier(gameStat.multiplier);
        return gs;
    }
}

module.exports = GameStatsFactory;