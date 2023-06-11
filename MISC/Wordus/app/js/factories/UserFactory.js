const User = require("../classe/User");

class UserFactory {
    getFromSocket = user => {
        const u = new User(
            user.uuid,
            user.name,
            user.color,
            user.avatar
        );

        u.setCombos(user.combos);
        return u
    }
}

module.exports = UserFactory