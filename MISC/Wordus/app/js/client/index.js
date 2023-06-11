const {} = require('../functions')
const {setDefaultPseudo, updateSliders} = require('../client/views/index_views');
const {io} = require('socket.io-client')

const Notification = require('../classe/Notification')
const notification = new Notification(document)

const { setCookie, genRandomAvatar, randomPseudo } = require('../functions');

document.addEventListener('DOMContentLoaded', () => {
    //notification.dialog('Cookie usage', 'Nous utilisont des cookies afin de stoker des informations relatives au jeu, Cela vous derange t\'il ?', ['yes', 'no'], notification.types.INFO, notification.img.COOKIE)

    const play_smart = document.querySelector('.play_smartphone')
    play_smart.addEventListener('click', () => {
        document.querySelector('.smartphone_use').style.display = "none"
        document.querySelector('body.new_game form').style.display = "flex"
    })

    const socket = io();

    //setDefaultPseudo(randomPseudo())
    updateSliders()

    let new_avatar = genRandomAvatar();
    document.getElementById('avatar').setAttribute('src', '../src/img/'+new_avatar)
    /* Génère un nouvel avatar aléatoirement */
    const randomAvatar = document.getElementById('random_avatar');
    randomAvatar.addEventListener('click', () => {
        new_avatar = genRandomAvatar();
        document.getElementById('avatar').setAttribute('src', '../src/img/'+new_avatar)
    });

    /**
     * Lorsque le client envoie le formulaire pour créer la room
     */
    const createRoomForm = document.getElementById('create_room')
    createRoomForm.addEventListener('submit', (e) => {
        e.preventDefault();

        const gameDuration = document.getElementById('game_duration').value;
        const wordAmount = document.getElementById('words-number').value;
        const lang = document.getElementById('lang').value
        const name = document.getElementById('name').value !== ''?
            document.getElementById('name').value :
            randomPseudo();
        const avatar = document.getElementById('avatar').getAttribute('src');

        if (name.length < 6) return notification.new('incorrect pseudo', 'Merci de Spécifier un pseudo de plus de 6 caratères.', notification.types.WARNING)

        if (name.length > 20) return notification.new('incorrect pseudo', 'Merci de Spécifier un pseudo de moins de 16 caratères.', notification.types.WARNING)

        /**
         * Par défault le créateur de la room est en jaune (sans doute le passer coté serveur pour éviter les soucis)
         * Les préférences par défault sont :
         *      - 60s
         *      - 5w
         *      - lat
         */
        const color = 'yellow';
        const preferences = {gameDuration, wordAmount, lang};

        /**
         * Envoie une demande au server pour créer une nouvelle room
         * Le server crée un nouveau utilisateur qu'il ajoute a la room automatiquement
         */
        socket.emit('host_room', preferences, name, color, avatar);
    });

    /**
     * Quand le serveur a bien créé la room il renvoit un event
     * Une fois l'event recu par le client il crée deux cookies
     *  - un pour l'UUID
     *  - un pour le code de la room
     * Ensuite le client est redirigé vers la pgae game
     */
    socket.on("success_host_room", (code, uuid) => {
        setCookie("uuid", uuid, 1);
        setCookie("code", code, 1);

        window.location.replace("/game");
    });
});