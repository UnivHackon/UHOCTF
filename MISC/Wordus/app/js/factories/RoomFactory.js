const Room = require("../classe/Room");

const UserFactory = require('./UserFactory');
const UF = new UserFactory();

const GameFactory = require('./GameFactory');
const GF = new GameFactory();

class RoomFactory {
    getFromSocket = room => {
        const r = new Room(
            room.code,
            UF.getFromSocket(room.owner),
            room.preferences
        );

        r.setGame(GF.getFromSocket(room.game));

        for (const k in room.users) {
            r.addUser(UF.getFromSocket(
                room.users[k]
            ));
        }
        return r;
    }
}

module.exports = RoomFactory;