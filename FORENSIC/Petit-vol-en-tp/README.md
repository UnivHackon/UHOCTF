# Petit vol en TP (INTRO)

## Auteur(s) :
`Senkei`

## Catégorie :
`Forensic`

## Description :
Un élève mal intentionné a capturé le trafic réseau de son poste pendant que son professeur se connectait pour y récupérer un fichier.

Quels sont le nom d'utilisateur et le mot de passe qu'a utilisé le professeur.

[tplab.pcap](./tplab.pcap)

**Flag** : `UHOCTF{user:passwd}`

---

# Solution

On a un fichier pcap, on l'ouvre avec wireshark et on cherche un peu.

![Wireshark](https://i.imgur.com/ym2Owoj.png)!

En examinant un peu les paquets, on voit que TELNET est utilisé, on peut donc utiliser le filtre `telnet` pour ne voir que les paquets telnet.

![Telnet](https://i.imgur.com/gvSqiOJ.png)!


Il suffit de --> Follow --> TCP Stream pour voir le contenu des paquets telnet.

![Follow](https://i.imgur.com/wVC0HB5.png)!


On peut maintenant filtrer les échanges entre le poste de l'élève et le poste du professeur et voir le username et le password.

![User](https://i.imgur.com/4fqUa49.png)!

**Flag** : `UHOCTF{tpuser:T3lN3t_iS_n3t_Secure!!}`


