# Evaluation Surprise !

Level - Introduction

Description:
```

Les premières années doivent apprendre les rudiment de la programmation. Ils doivent écrire leurs première calculatrice !

Vérifier vos input !

`nc huoctf.fr 40013`
```

## Instructions:

Les étudiants ont des calculs qu'ils doivent faire. Ils doivent donc faire un programme qui prend en entrée une chaine de charactère et qui renvoie le résultat du calcul.


## Solution


## Hosting
This challenge should be a Docker container that runs `python3 chall.py` on port 40014. All the proper files are included in here. The command to build the docker container is (when located inside of this directory):

```bash
 docker build -t evaluation-suprise .
 docker network create -d bridge evaluation-suprise
```

The command to start the challenge is:

```bash
 docker run -p 40002:40000 --detach --name evaluation-suprise --network evaluation-suprise evaluation-suprise:latest
```

The command to stop the challenge (since CTRL+C won't work) is:

```bash
 docker stop evaluation-suprise
```


**Flag** - `UHOCTF{Ev3LuAtI0nS*rPise}`
