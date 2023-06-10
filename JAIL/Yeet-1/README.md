# Yeet 1 (INTRO)

## Auteur(s)
`Senkei`

## Catégorie
`Jail`

## Description:
Un étudiant te propose un petit défi. Ne cherche pas trop loin !

**Flag** : `UHOCTF{Fake_flag}`

[yeet.py](src/yeet.py)

---

## Solution

```python
eval(ord('╬')) = 9580
```

Il suffit d'envoyer `ord('╬')` pour avoir le flag.

**Flag** - `UHOCTF{J4IL_CE_PL4ISIR}`

## Hosting

This challenge should be a Docker container that runs `python3 chall.py` on port 40014. All the proper files are included in here. The command to build the docker container is (when located inside of this directory):

```bash
sudo docker build -t yeet1 .
sudo docker network create -d bridge yeet1
```

The command to start the challenge is:

```bash
sudo docker run -p 40020:40020 --detach --name yeet1 --network yeet1 yeet1:latest
```

The command to stop the challenge (since CTRL+C won't work) is:

```bash
sudo docker stop yeet1
```

