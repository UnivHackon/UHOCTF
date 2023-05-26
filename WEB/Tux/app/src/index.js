const cookieParser = require('cookie-parser')
const express = require('express')
const { exec } = require("child_process");

const PORT = process.env.PORT || 3000;

const app = express();
app.set('view engine', 'ejs');
app.use(express.json());
app.use(cookieParser());

class Tux {
    constructor(value, defaultLength){
        this.value = value
        this.defaultLength = defaultLength
    }

    async getTux(){
        if (!this.value) {
            // Use 'fortune' to generate a random funny line, based on the input size
            try {
                this.value = await execCowSayWithFortune(this.defaultLength)
            } catch (error) {
                this.value = 'Error while getting a funny line'
            }
        } else if (typeof this.value === 'string' && !this.value.includes('flag')) {
            try {
                this.value = await execCowSay(this.value)
            } catch (error) {
                this.value = 'Error while getting a funny line'
            }
        } else {
            this.value = 'No flag for you'
        }
        return this.value
    }
}

app.get('/', async (req, res) => {
    res.render('index');
});

app.post('/generate', async (req, res) => {
    const { value } = req.body;
    console.log(value)
    try {
        let newCow;
        // If the length is too long, we use a default according to the length
        if (value.length > 154)
            newCow = new Tux(null, value.lenght)
        else {
            newCow = new Tux(String(value))
        }

        const code = await newCow.getTux()
        res.json({ code });
    } catch (error) {
        res.status(422).json({ message: "error", reason: 'Unknow error' });
    }
});

function execCowSayWithFortune(defaultLength) {
    return new Promise((resolve, reject) => {
        exec(`fortune -n ${defaultLength} | cowsay -f tux`, (error, stdout, stderr) => {
            console.log(stdout, stderr, error)
            if (error) reject(error);
            resolve(stdout? stdout : stderr);
        });
    });
}

function execCowSay(defaultLength) {
    return new Promise((resolve, reject) => {
        exec(`cowsay -f tux ${defaultLength}`, (error, stdout, stderr) => {
            console.log(stdout, stderr, error)
            if (error) reject(error);
            resolve(stdout? stdout : stderr);
        });
    });
}

app.listen(PORT, async () => {
    console.log(`Cow Generator is running on port ${PORT}`);
});