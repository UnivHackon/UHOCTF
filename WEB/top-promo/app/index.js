const express = require("express");
const app = express();
const path = require("path");


app.use(express.urlencoded({ extended: true })); // Middleware pour traiter les données POST

app.get('/', function(req, res) {
    res.sendFile(path.join(__dirname, '/index.html'));
});

app.post('/ajouter', function(req, res) {
    // Récupérer les données du formulaire
    const id = req.body.id;
    const nom = req.body.nom;
    const classement = req.body.classement;
    const signature = req.body.signature;

    if(signature == calculerSignature(classement)) {
        return res.status(200).send({"data":process.env.FLAG});
    } else {
        return res.status(400).send({"data":'Vilain tricheur ! '});
    }

});


app.listen(3000, () => {
    console.log("App listening on port 3000");
});

function calculerSignature(note) {

    const signature = Math.pow(note, 3) + Math.sqrt(note) + Math.log(note);

  return signature;
}