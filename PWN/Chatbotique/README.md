# Chatbotique (MEDIUM)

## Auteur(s) :

`Hokanosekai`

## Catégorie : 

`Pwn`

## Description :

Résoudre tous les calcules en moins de 1min.

`nc 161.35.21.37 40013`

**Flag** : `UHOCTF{fake_flag}`

---

## Solution

**Flag** : `UHOCTF{C4lcul3s_3t_3xpr3ss10ns_M4gn1f1qu3s!}`

## Hosting

```bash
sudo docker build -t chatbotique .
sudo docker network create -d bridge chatbotique
```

The command to start the challenge is:

```bash
sudo docker run -p 40013:40013 --detach --name chatbotique --network chatbotique chatbotique:latest
```

The command to stop the challenge (since CTRL+C won't work) is:

```bash
sudo docker stop chatbotique
```
