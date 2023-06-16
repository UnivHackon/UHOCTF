# Secret Passwd (HARD)

## Auteur(s) :
`Senkei`

## Catégorie :
`Forensic`

## Description :

Il y a encore un mot de passe que tu n'as pas trouvé...

**Flag** : `UHOCTF{password0123}`

---

## Solution :


Dans le challenge Ciscolaire il y a un hash différent qui est donné. On peut donc supposer que c'est le hash du mot de passe que l'on cherche.

```bash
enable secret 5 $1$uWu$AqVCwW92Lrt.V3SnNC1mS.
```

Pour commencer je vais faire une petite wordlist avec les éléments du ctf pour composer ma wordlist.


```plain

hack
hackon
on
univ
univhackon
university
la-rochelle
lr
17000
17
naruto
dragodinde
```

A partir de cela je vais concatener les mots entre eux pour avoir une wordlist plus complète.

```bash
# ( J'utilise fish)

bash -c 'for i in (cat words.txt); for j in (cat wordlist.txt); echo $i$j; end; end' > wordlist2.txt


```



**Flag** : `UHOCTF{UHOCTF_univlr17}`