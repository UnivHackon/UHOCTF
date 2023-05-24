# Avocat Enigmatique (INTRO)

## Auteur(s) :

`Hokanosekai#1033`

## Catégorie : 

`crypto`

## Description :

Décrypter le message suivant :

`Vk zvksnys|so kymk~skvo o}~ x k|~ }l~sv`

**Flag** : `UHOCTF{message_original}`

## Solution :

On remarque dans le titre "Avocat", sous une autre lecture, on peut lire "A vaut K", ce qui nous fait penser à un chiffrement par décalage.

Ici, on peut facilement en deviner le décalage, il suffit de regarder la valeur de la lettre `a` ou `A` et `k` ou `K` dans la table ASCII, qui est 97, 65, 107, 75 respectivement.

Donc `107 - 97 = 10` et `75 - 65 = 10`, on peut donc en déduire que `K = A + 10` et `k = a + 10`.

On peut donc facilement déchiffrer le message.

Pour automatiser le déchiffrement, on peut utiliser un script python :

```python
def decrypt(message):
    decrypted = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                decrypted += chr((ord(char) - 65 - 10) % 26 + 65)
            else:
                decrypted += chr((ord(char) - 97 - 10) % 26 + 97)
        else:
            decrypted += char
    return decrypted

print(decrypt("Vk zvksnys|so kymk~skvo o}~ x k|~ }l~sv"))
```

**Flag** : `UHOCTF{La_plaidoirie_avocatiale_est_un_art_subtil}`