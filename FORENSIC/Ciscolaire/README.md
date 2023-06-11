# Ciscolaire (EASY)

## Auteur(s) :
`Senkei`

## Catégorie : 
`Forensic`

## Description :

Un élève à réussit à mettre la main sur un routeur Cisco. Il a réussit à récupérer la config mais il n'arrive pas à trouver le mot de passe admin. Quelle est le mot de passe de senkei ?

[cisco.conf](./cisco.conf)

**Flag** : `UHOCTF{password0123}`

--- 

## Solution :
```
Type 7 mdp non sécu

Hoka : UHOCTF_escalope
Zyksa : UHOCTF_dragodinde
??? : UHOCTF_p@ass


 On voit qu'on commence avec UHOCTF_

Ducoup je créer une wordlist custom avec rockyou:

sed -i -e '/s/^/UHOCTF_/' rockyou


Et on peux bruteforce le mdp de senkei :

`john  --wordlist=./uho_wl.txt ./pass.txt`

https://i.imgur.com/LhQqfFF.png
$1$uWu$dVdb41eRcD.np7zCwgUgU1
```





**Flag** : `UHOCTF{UHOCTF_naruto}`
