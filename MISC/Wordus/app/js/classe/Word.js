class Word {
    word
    length
    letters = []
    position

    users = {}

    constructor(word, position) {
        this.word = word;
        this.length = word.length
        this.letters = word.split('');
        this.position = position;
    }

    addUser = (uuid, color) => {
       if (!this.users[uuid]) this.users[uuid] = color;
    }

    removeUser = (uuid) => {
        if (this.users[uuid]) delete this.users[uuid]
    }

    getUsers = () => {
        return this.users;
    }

    getLength = () => {
        return this.length;
    }

    getLetters = () => {
        return this.letters;
    }

    getWord = () => {
        return this.word;
    }

    getPosition = () => {
        return this.position;
    }

    include = (word_input) => {

        let letters_input = word_input.split('')
        let inputSize = word_input.length
        let letters = this.letters.slice(0,inputSize)
        return arraysEqual(letters, letters_input)
    }

    equalWord = (word) => {
        return this.word === word;
    }

    getNbUsers = () => {
        return Object.keys(this.users).length;
    }
}

function arraysEqual(a, b) {
    if (a === b) return true;
    if (a == null || b == null) return false;
    if (a.length !== b.length) return false;
    for (var i = 0; i < a.length; ++i) {
        if (a[i] !== b[i]) return false;
    }
    return true;
}

module.exports = Word