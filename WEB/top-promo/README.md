# Top Promo (EASY)

## Auteur(s) :
`Senkei`

## Catégorie :
`Web`

## Description :

Triche et valide ton année.

[https://top-promo.univhackon.fr](https://top-promo.univhackon.fr/)

**Flag** : `UHOCTF{Fake_flag}`

---

## Solution

Pour ce challenge, il faut envoyer une requête POST avec les paramètres `note` et `signature` à l'URL `https://top-promo.univhackon.fr/validate`.

```js
xhr.send(`note=${note}&signature=0`);
```
Quand on essaye de faire un poste en curl on obtient :



```bash
curl -X POST -d 'note=20&signature=0' https://top-promo.univhackon.fr/ajouter


curl: (6) Could not resolve host: application

{"data":"Vilain tricheur ! ","message":"La signature est incorrecte !"}

```

On comprend qu'il faut modifier la signature pour que la requête soit valide et il y a deux function qui sont données dans le code source de la page :

```js
    const a=function(b){return Math.pow(b,3)+Math.sqrt(b)+Math.log(b)};

    const ab=function(c){return Math.pow(c,6)+ Math.pow(c,5)+ Math.pow(c,4)+ Math.pow(c,3)+ Math.pow(c,2)+c};
```
Elles prennent un param donc on peut se dire que c'est la note.

On peut les exécuter directement dans le navigateur, F12 -> console :

```js
a(20)
8007.467868228553 

```
et 

```js
ab(20)
67368420 
```

On essaye d'envoyer ceci en signature :

```bash
curl -X POST -d 'note=20&signature=8007.467868228553' https://top-promo.univhackon.fr/ajouter

{"data":"UHOCTF{ANNEE_VALIDEE}"}

```




**Flag** - `UHOCTF{ANNEE_VALIDEE}`


