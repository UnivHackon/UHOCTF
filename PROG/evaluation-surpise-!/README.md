# Evaluation Surprise ! (INTRO)

#### Auteur(s)
`Senkei`

#### Catégorie
`Prog`

#### Description:

Les premières années doivent apprendre les rudiments de la programmation. Ils doivent écrire leur première calculatrice !

Vérifier vos inputs !

**Flag** : `UHOCTF{Fake_flag}`


## Solution


**Flag** - `UHOCTF{Ev3LuAtI0nS*rPise}`


## Hosting

```bash
 docker build -t evaluation-suprise .
 docker network create -d bridge evaluation-suprise
```

The command to start the challenge is:

```bash
 docker run -p 40001:40001 --detach --name evaluation-suprise --network evaluation-suprise evaluation-suprise:latest
```

The command to stop the challenge (since CTRL+C won't work) is:

```bash
 docker stop evaluation-suprise
```


