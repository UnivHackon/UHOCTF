# T'as la référrrrrence ?

Level - Medium

Auteur - Senkei

Description:
```

On dirait que le service admin de l'université n'est pas totalement sécurisé.

J'ai besoin de ton aide pour contourner le système!

```

## Instructions:

Un étudiant te propose un petit défi. 

## Solution


En regardant les sources on peut comprendre



## Hosting
This challenge should be a Docker container that runs `python3 chall.py` on port 40014. All the proper files are included in here. The command to build the docker container is (when located inside of this directory):

```bash
sudo docker build -t referrrence .
sudo docker network create -d bridge referrrence
```

The command to start the challenge is:

```bash
sudo docker run -p 40018:40000 --detach --name referrrence --network referrrence referrrence:latest
```

The command to stop the challenge (since CTRL+C won't work) is:

```bash
sudo docker stop referrrence
```


**Flag** - `UHOCTF{f4uT_La_Tr0uve3_cte_REF}`
