class GameStats {
    score
    multiplier

    constructor() {
        this.resetMultiplier();
        this.resetScore();
    }

    resetScore = () => {
        this.score = 0;
    }

    resetMultiplier = () => {
        this.multiplier = 1;
    }

    getScore = () => {
        return this.score;
    }

    getMultiplier = () => {
        return this.multiplier;
    }

    addPoints = (points) => {
        this.score += Math.floor(points);
    }

    removePoints = (points) => {
        this.score -= points;
    }

    addMultiplier = (coeff) => {
        this.multiplier += coeff;
    }

    setScore = (score) => {
        this.score = score;
    }

    setMultiplier = (multiplier) => {
        this.multiplier = multiplier;
    }
}

module.exports = GameStats;