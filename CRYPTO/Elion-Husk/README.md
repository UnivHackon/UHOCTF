# Elion Husk (EASY)

## Auteur(s) :

`Hokanosekai`

## Catégorie : 

`Crypto`

## Description :

Un de tes camarades a intercepté un message entre deux étudiants de la mention Mathématiques. Aide-le à le décrypter.

![encrypted](https://i.imgur.com/2OPlfZ4.png)

**Flag** : `UHOCTF{Fake_flag}`

---

## Solution

On peut voir que le message est constitué de caractères mathématiques. 

Grâce au pdf [LATEX Mathematical Symbols](https://www.cmor-faculty.rice.edu/~heinken/latex/symbols.pdf), on peut facilement retrouver les caractères utilisés.

```latex
\Upsilon \Hat \Omega \Cap \Theta \Finv { \Pi \ltimes \aleph y \_ \wp \infty \therefore \heartsuit \_ \Lsh \aleph \Theta \eth \Xi }
```

Enfin, on constate que c'est la première lettre de chaque mot qui forme le flag.

**Flag** : `UHOCTF{Play_with_LaTeX}`
