const { log } = require("console");
const express = require("express");
const app = express();
const path = require("path");
//load env
require('dotenv').config();

app.use(express.urlencoded({ extended: true })); // Middleware pour traiter les données POST

app.get('/', function(req, res) {
    res.sendFile(path.join(__dirname, '/index.html'));
});

app.post('/ajouter', function(req, res) {
    // Récupérer les données du formulaire
    console.log(req.body)
    const id = req.body.id;
    const nom = req.body.nom;
    const note = req.body.note;
    const signature = req.body.signature;

    console.log("id : " + calculerSignature(note) + " " + signature);
    if(signature == calculerSignature(note)) {
        return res.status(200).send({"data":process.env.FLAG});
    } else {
        return res.status(400).send({"data":'Vilain tricheur ! ',"message":"La signature est incorrecte !"});

    }

});


app.listen(3000, () => {
    console.log("App listening on port 3000");
});

function calculerSignature(note) {

    const signature = Math.pow(note, 3) + Math.sqrt(note) + Math.log(note);

  return signature;
}