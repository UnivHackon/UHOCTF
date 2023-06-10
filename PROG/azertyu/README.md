# Les claviers c'est pas facile quand ça veut pas (EASY)

#### Auteur(s)
`Senkei`

#### Catégorie
`Prog`

#### Description:

Le pauvre étudiant n'arrive plus à utiliser son clavier. Il a besoin de votre aide pour corriger ses erreurs.

**Flag** : `UHOCTF{Fake_flag}`

---

## Solution


## Hosting

```bash
sudo docker build -t azertyu .
sudo docker network create -d bridge azertyu
```

The command to start the challenge is:

```bash
sudo docker run -p 40000:40000 --detach --name azertyu --network azertyu azertyu:latest
```

The command to stop the challenge (since CTRL+C won't work) is:

```bash
sudo docker stop azertyu
```


**Flag** - `UHOCTF{LeS_cL4vIeRs_c'3sT_pQs_f4c1l3_S8R_Z1Nd3UBE!}`
