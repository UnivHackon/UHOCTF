const {setCookie, genRandomAvatar, randomPseudo} = require('../functions')
const {setColor, setDefaultPseudo} = require('../client/views/join_views');
const {io} = require("socket.io-client");

const Notification = require('../classe/Notification')
const notification = new Notification(document)

document.addEventListener('DOMContentLoaded', () => {
    const socket = io();

    /* Récupération du code de la room dans l'URL */
    var code = location.search.slice(1);

    let new_avatar = genRandomAvatar();
    document.getElementById('avatar').setAttribute('src', '../src/img/'+new_avatar)

    /* Génère un nouvel avatar aléatoirement */
    const randomAvatar = document.getElementById('random_avatar');
    randomAvatar.addEventListener('click', () => {
        new_avatar = genRandomAvatar();
        document.getElementById('avatar').setAttribute('src', '../src/img/'+new_avatar)
    });

    /**
     * Vérifie si la room passer en url existe
     */
    var color = 'pink';
    socket.emit('exist_room', code);
    socket.on('room_exist', res => {
        color = res;
        setColor(color);
    });

    /**
     * Si la room n'existe pas :
     */
    var noRoom = false;
    socket.on('no_room', () => {
        noRoom = true;
        console.log(noPlace, noRoom)
    });

    /**
     * Si le nombres d'utilisateurs est déja atteint
     */
    var noPlace = false;
    socket.on('no_place', () => {
        noPlace = true;
        console.log(noPlace, noRoom)
    });

    //setDefaultPseudo(randomPseudo());

    /**
     * Lorsque le client envoie le formulaire pour rejoindre la room
     */
    const joinRoomForm = document.getElementById('join_room');
    joinRoomForm.addEventListener('submit', (e) => {
        e.preventDefault();

        const name = document.getElementById('name').value !== ''?
            document.getElementById('name').value :
            randomPseudo();
        const avatar = document.getElementById('avatar').getAttribute('src');

        if (name.toLowerCase().includes('flag')) return notification.new('flag', 'UHOCTF{7h1s_n07_7h3_fl4g}', notification.types.SUCCESS, 5)

        if (name.length < 6) return notification.new('incorrect pseudo', 'Merci de spécifier un pseudo de plus de 6 caractères', notification.types.WARNING, 5)

        if (name.length > 20) return notification.new('incorrect pseudo', 'Merci de Spécifier un pseudo de moins de 16 caratères.', notification.types.WARNING)

        if (noRoom) return notification.new('no room find', `La room à laquelle vous tentez d\'acceder n\'existe pas, vérifiez si le code renseigné est le bon. <br>Sinon vous pouvez toujours créer une nouvelle room <a href="/">ICI</a>`, notification.types.ERROR)

        if (noPlace) return notification.new('limit of players reached', `La room à laquelle vous tentez d\'acceder est déja complete. <br>Vous pouvez toujours créer une nouvelle room <a href="/">ICI</a>`, notification.types.ERROR)

        /**
         * Envoie la demande au serveur pour créer l'utilisateur et l'ajouter a la room
         */
        socket.emit('create_user', code, name, color, avatar);
    });

    /**
     * Event reçu du serveur après la création de l'utilisateur
     * Deux nouveau cookie sont enregisté :
     *  - code
     *  - uuid
     * Redirection du client vers la page /game de la room
     */
    socket.on('created_user', (code, uuid) => {
        setCookie("uuid", uuid, 1);
        setCookie("code", code, 1);

        window.location.replace("/game");
    });
});