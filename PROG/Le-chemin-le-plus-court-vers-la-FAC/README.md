# Plus court ou plus rapide ? (HARD)

## Auteur(s) :

`Hokanosekai`

## Catégorie : 

`Prog`

## Description :

Tous les jours, je me rends à la fac en bus. Mais aujourd'hui, le bus est en panne. Je dois donc trouver un autre moyen de transport. Je me rends compte que je peux prendre le métro. Mais je ne sais pas quel est le chemin le plus court pour aller à la fac. Pouvez-vous m'aider ?

`nc {ip} {port}`

Exemple de graphe créé par le serveur :

```json
{
  "graph": {
    "nodes": ["A", "B", "C"],
    "edges": [
      {"source": "A", "target": "B", "weight": 5},
      {"source": "B", "target": "C", "weight": 3},
      {"source": "A", "target": "C", "weight": 10}
    ]
  },
  "source": "A",
  "destination": "C"
}
```

Puis on retourne sous le format suivant :

```text
A B 5
B C 3
A C 10
-----
A > C
```

Exemple de réponse attendue :

```json
{
  "path": ["A", "B", "C"],
  "weight": 8
}
```

**Flag** `UHOCTF{Fake_flag}`

---

## Solution :

