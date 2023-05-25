# Petit hacking en salle de  tp

Niveau - Introduction

Auteur - Senkei

## Description

Auteur : Senkei

```

Un elève mal attentionné a capturé le trafic réseau de son poste pendant que son professeur se connectait pour y recupérer un fichier.

Quel est le nom d'utilisateur et le mot de passe qu'a utilisé le professeur ?
```


Format du flag : UHOCTF{user:passwd}



# Solution


On a un fichier pcap, on l'ouvre avec wireshark et on cherche un peu.

![Wireshark](https://i.imgur.com/ym2Owoj.png)!

En examinant un peu les paquets, on voit que TELNET est utilisé, on peut donc utiliser le filtre `telnet` pour ne voir que les paquets telnet.

![Telnet](https://i.imgur.com/gvSqiOJ.png)!


Il suffit de --> Follow --> TCP Stream pour voir le contenu des paquets telnet.

![Follow](https://i.imgur.com/wVC0HB5.png)!


On peut maintenant filtrer les échanges entre le poste de l'élève et le poste du professeur et voir le username et le password.

![User](https://i.imgur.com/4fqUa49.png)!


On a donc le flag : UHOCTF{tpuser:T3lN3t_iS_n3t_Secure!!}


