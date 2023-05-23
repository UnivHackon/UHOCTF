# Les claviers c'est pas facile quand ça veut pas

Level - Facile

Description:
```
Le pauvre étudiant n'arrive plus à utiliser son clavier. Il a besoin de votre aide pour corriger ses erreurs.

Renvoyer les mots corrigé.

`nc huoctf.fr 40014`
```

## Instructions:

L'étudiant reçois des chaines de charactères étrange...
C'est enfaite des strings qui sont transformé de azerty vers qwerty.

Il faut donc faire l'inverse pour retrouver le flag.


## Solution


## Hosting
This challenge should be a Docker container that runs `python3 chall.py` on port 40014. All the proper files are included in here. The command to build the docker container is (when located inside of this directory):

```bash
sudo docker build -t azertyu .
sudo docker network create -d bridge azertyu
```

The command to start the challenge is:

```bash
sudo docker run -p 40014:40000 --detach --name azertyu --network azertyu azertyu:latest
```

The command to stop the challenge (since CTRL+C won't work) is:

```bash
sudo docker stop azertyu
```


**Flag** - `UHOCTF{LeS_cL4vIeRs_c'3sT_pQs_f4c1l3_S8R_Z1Nd3UBE!}`
