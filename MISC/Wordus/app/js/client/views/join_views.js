/**
 * Update la couleur du boutton et de la bordure en fonction d'un nombre de joueurs deja present dans la partie
 *
 * @param color
 */
function setColor(color) {
    const avatarBorder = document.getElementById('avatar');
    avatarBorder.classList.forEach(c => {
        avatarBorder.classList.remove(c);
    });
    avatarBorder.classList.add('color-'+color);

    const avatarBtn = document.getElementById('random_avatar');
    avatarBorder.classList.forEach(c => {
       avatarBtn.classList.remove(c);
    });
    avatarBtn.classList.add('color-'+color);
}

/**
 * Met un pseudo (definis aleatoirement) dans l'input du pseudo
 *
 * @param pseudo
 */
function setDefaultPseudo(pseudo) {
    const name = document.getElementById('name')
    name.setAttribute('value', pseudo);
}

module.exports = {
    setColor,
    setDefaultPseudo
}