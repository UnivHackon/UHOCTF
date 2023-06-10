# Top Promo (EASY)

## Auteur(s) :
`Senkei`

## Catégorie :
`Web`

## Description :

Triche et valide ton année.

**Flag** : `UHOCTF{Fake_flag}`

---

## Solution



**Flag** - `UHOCTF{N0n_J3_RigolE_Tu_Peux_Resterehe}`

## Hosting
This challenge should be a Docker container that runs `python3 chall.py` on port 40014. All the proper files are included in here. The command to build the docker container is (when located inside of this directory):

```bash
sudo docker build -t laliste .
sudo docker network create -d bridge laliste
```

The command to start the challenge is:

```bash
sudo docker run -p 40015:40000 --detach --name laliste --network laliste laliste:latest
```

The command to stop the challenge (since CTRL+C won't work) is:

```bash
sudo docker stop laliste
```

