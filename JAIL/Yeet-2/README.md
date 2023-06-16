# Yeet 1 (EASY)

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


On peux voir que le 0 n'est pas pris dans le regex -> il faut utiliser l'hexadécimal.

```python
9580 / 15 (0xf) = 638 
0xa = 10
payload = "0xf+"*638 + "0xa"
```

**Flag** - `UHOCTF{W0w_Tr00p_F4c1l3?}`

## Hosting
This challenge should be a Docker container that runs `python3 chall.py` on port 40014. All the proper files are included in here. The command to build the docker container is (when located inside of this directory):

```bash
sudo docker build -t yeet2 .
sudo docker network create -d bridge yeet2
```

The command to start the challenge is:

```bash
sudo docker run -p 40021:40021 --detach --name yeet2 --network yeet2 yeet2:latest
```

The command to stop the challenge (since CTRL+C won't work) is:

```bash
sudo docker stop yeet2
```
