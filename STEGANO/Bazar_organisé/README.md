# Bazar organisé

## Auteur(s) :
`Reyko`

## Niveau :
`Medium`

## Catégorie :
`Stegano`

## Description :

Vous recevez un message d’un vieil ami d’enfance à qui vous n’avez pas parler depuis de nombreuses années. Il vous rappelle que vous aviez créé une énigme pour y cacher un message secret, cependant vous avez tous deux oubliés la manière de retrouver ce message secret…

Pour retrouver le message, votre vieil ami vous a transmis 2 informations capitales :
 - Un texte composé de mots divers et variés.
- Son numéro porte bonheur : le numéro 8 en ajoutant qu’il est très attaché a ce numéro et qu’il a surement une importance.

## Consigne :

Retrouvez le message secret dans le texte ci-dessous.
Une technique spécifique de stéganographie devra être utilisée.

**Flag** `UHOCTF{un_message_secret}`

## Solution :

La technique à utiliser est le code de Barne.
Explication codee de Barne : https://www.apprendre-en-ligne.net/crypto/stegano/barncode.html

Tableau Pour la résolution du code de Barne : 

| C | A | U | C | A | S | S | E |
|---|---|---|---|---|---|---|---|
| 3 | 1 | 8 | 4 | 2 | 6 | 7 | 5 |


| C | A | U | C | A | S | S | E |
|---|---|---|---|---|---|---|---|
| Oubli | Un | Cochon | Cicatrice | Information | Plaquettaire | Miel | Caucasse |
| Exploiter | Riz | Coton | Unique | Très | Contre | Nouvelles | Films |
| Voici | Machette | Chiffon | Lac | Logs | Mousse | Dramatique | Coma |
| Luciole | Principal | Effrayant | Message | Pie | Sol | Sentier | Banque |
| Commentaire | Très | Animal | Perdre | Mordre | Soupe | Fini | Intéréssant |
| Architecte | Séance | Seul | Cortex | Le | Secret | Pluriel | Monochrome |
| Baignade | Nouvelles | Observatoire | Branche | Sciage | Six | Et | Dur |
| Adulte | Battre | Fabuleux | Sel | Faucille | Perspective | Orchestre | Bonbons |
| Plier | Insecticide | Poésie | Carotte | Banane | Parapluie | Dentiste | Roue |


**Flag** `UHOCTF{voici_un_fabuleux_message_tres_secret_et_interessant}`