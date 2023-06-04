# Wordus (EASY)

## Auteur(s) :

`Hokanosekai`

## Niveau :

`Medium`

## Catégorie : 

`Misc`

## Description :

Voici le site web créé par des étudiants de la promo lors d'une gamejam. Ils ont caché un flag quelque part, saurez-vous le retrouver ?

`wordus.xyz`

> Note : Uniquement pour ce challenge, les joueurs sont autorisés à utiliser des outils d'énumération sur le serveur. (Toute autre attaque non autorisée sera sanctionnée)

**Flag** `UHOCTF{Fake_flag}`

---

## Solution :

On peut commencer par faire un scan de ports avec nmap :

```bash
nmap -sV -sC -p- wordus.xyz
```

On obtient :

```bash
PORT     STATE SERVICE VERSION
80/tcp   open  http    nginx 1.14.2
|_http-server-header: nginx/1.14.2
|_http-title: Wordus
25565/tcp open minecraft Minecraft 1.19.4 (Protocol: 754)
```

On voit deux informations intéressantes :

- Le serveur web est un nginx
- Il y a un serveur minecraft

On peut donc commencer par regarder le site web.

Très on peut s'appercevoir que le site web est une impasse, il n'y a rien d'intéressant.

On peut donc se tourner vers le serveur minecraft.

On s'y connecte avec un client minecraft et on se retrouve dans un monde vanilla en 1.19.4.

On peut commencer par regarder les commandes disponibles avec la commande `/help`.

On remarque deux commandes :

- `/wordus`
- `/flag`

La commande `/flag` nous kick du serveur.

Enfin la commande `/wordus` nous donne le flag.

**Flag** `UHOCTF{w0rdus_1s_4w3s0m3}`