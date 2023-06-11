class User {
    uuid
    name
    color
    avatar
    combos

    constructor(uuid, name, color, avatar) {
        this.uuid = uuid;
        this.name = name;
        this.color = color;
        this.avatar = avatar;
        this.resetCombos();
    }

    resetCombos = () => {
        this.combos = 0;
    }

    addCombos = () => {
        this.combos += 1
    }

    getCombos = () => {
        return this.combos;
    }

    setCombos = (combos) => {
        this.combos = combos;
    }

    getUUID = () => {
        return this.uuid;
    }

    getName = () => {
        return this.name;
    }

    getInfo = () => {
        return {color: this.color, avatar: this.avatar};
    }

    setInfo = (color, avatar) => {
        this.color = color;
        this.avatar = avatar;
    }
}
module.exports = User
