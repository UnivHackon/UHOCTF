/**
 * Met un pseudo (definis aleatoirement) dans l'input du pseudo
 *
 * @param pseudo
 */
function setDefaultPseudo(pseudo) {
    const name = document.getElementById('name')
    name.setAttribute('value', pseudo);
}

/**
 * Update range sliders (animation) :
 *  - game duration
 *  - word amount
 */
function updateSliders() {
    const gameDurationSliderValue = document.querySelector('.game-duration.range .slider-value span')
    const wordsNumberSliderValue = document.querySelector('.words-number.range .slider-value span')

    const gameDurationInputSlider = document.querySelector('.game-duration.range input')
    const wordsNumberInputSlider = document.querySelector('.words-number.range input')

    gameDurationInputSlider.oninput = (() => {
        let value = gameDurationInputSlider.value
        gameDurationSliderValue.textContent = `${value} sec.`
        gameDurationSliderValue.style.left = (value*60 / 150) + 3 + '%'
    });

    wordsNumberInputSlider.oninput = (() => {
        let value = wordsNumberInputSlider.value
        let add = 6.428571428571429
        wordsNumberSliderValue.textContent = `${value} mots`
        wordsNumberSliderValue.style.left = (value * 60 / 7) + add + '%'
    });
}

module.exports = {
    setDefaultPseudo,
    updateSliders
}