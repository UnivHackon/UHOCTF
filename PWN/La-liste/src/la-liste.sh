#!/bin/bash

listePersonnes="Trugeon Bourmaud Besserer Demko Viaud"

echo "Bonjour à toi. Je sais que les professeurs de ton université veulent se débarrasser de toi, je me suis donc dépêché de t'obtenir la raison, elle est juste là dans le fichier raison.txt !

En attendant j'ai aussi obtenu des informations sur Trugeon, Bourmaud, Besserer, Demko et Viaud. De qui veux-tu que je te parle ?"
read personne
eval "grep -wie ^$personne informations.txt"
eval "ls"
while true; do
    echo "
De qui d'autre tu veux que je te parle ?"
    read personne

    if [ -n $personne ] && [ $personne = "stop" ] ; then
    exit
    fi

    bob=$(grep -wie ^$personne informations.txt)

    if [ -z "$bob" ]; then
        echo "Je n'ai pas compris de qui tu parlais. Dis-moi stop si tu veux que je m'arrête, et envoie l'un des noms que j'ai cités si tu veux des informations."
    else
        echo $bob
    fi

done