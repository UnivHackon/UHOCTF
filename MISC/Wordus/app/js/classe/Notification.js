const NotifyType = {
    WARNING: 1,
    ERROR: 2,
    INFO: 3,
    SUCCESS: 4
}

const ImgType = {
    COOKIE: 1,
    NOT_FOUND: 2,
    COFFEE: 3,
}

var counter = 0

module.exports = class Notifications {
    title
    reason
    type
    duration

    types = NotifyType

    img = ImgType

    document
    container
    element

    constructor(document) {
        this.document = document;
        this.container = document.querySelector('.notifications-container')
    }

    new = (title, reason, type, duration = 5) => {
        let classType
        switch (type) {
            case 1:
                classType = 'warning'
                break
            case 2:
                classType = 'error'
                break
            case 3:
                classType = 'info'
                break
            case 4:
                classType = 'success'
                break
        }

        let id = counter

        this.container.innerHTML += `
            <div id="${id}" class="notification ${classType} show">
                <span class="type">${classType.toUpperCase()} - ${title.toUpperCase()}</span>
                <p class="text">${reason}</p>
            </div>`
        this.element = this.document.getElementById(`#${counter}`)

        let startTime = Date.now()
        let t = setInterval(() => {
            document.querySelectorAll('.notification').forEach(el => {
                if (parseInt(el.id) === id && Date.now() - startTime > duration * 1000) {
                    this.container.removeChild(el)
                    clearInterval(t)
                }
                el.addEventListener('click', () => {
                    this.container.removeChild(el)
                    clearInterval(t)
                })
            })
        }, 1000)
        counter += 1
    }

    dialog = (title, reason, buttons = ['yes', 'no'], type, img) => {
        let classType
        switch (type) {
            case 1:
                classType = 'warning'
                break
            case 2:
                classType = 'error'
                break
            case 3:
                classType = 'info'
                break
            case 4:
                classType = 'success'
                break
        }

        let id = counter

        let t = ``
        buttons.forEach(btn => {
            t += `
                <div class="btn color-pink">
                    <p>${btn.toUpperCase()}</p>
                </div>`
        })

        this.container.innerHTML += `
            <div id="${id}" class="dialog ${classType} show">
                <span class="type">${classType.toUpperCase()} - ${title.toUpperCase()}</span>
                <p class="text">${reason}</p>
                <div class="buttons">${t}</div>
            </div>`
        this.element = this.document.getElementById(`#${counter}`)

        counter += 1
    }
}