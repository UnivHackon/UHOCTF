# Calculateur express! (EASY)

## Auteur(s) :

`Hokanosekai#1033`

## Catégorie : 

`pwn`

## Description :

Résoudre tous les calcules en moins de 1min.

`nc {IP} {PORT}`

**Flag** : `UHOCTF{fake_flag}`

---

## Instructions :

Le joueur doit résoudre différents calcul en trouvant l'opérateur associés aux nombres et au résultat de l'application de l'opérateur passé sur les deux nombres.

En cas de bonne réponse, on renvoie un nouveau problème tant qu'il n'a pas réussi 100 calculs. Une fois les 100 calculs atteint le joueur recevra le flag.

En cas de mauvaise réponse la connexion est coupée, un message d'erreur est envoyé et le joueur doit recommencer a zéro.

Si jamais le joueur venait a dépassé 1 min de connexion alors elle est coupée et un message de timeout est envoyé.

Dans cette première version les opérateurs sont limités a 4 :

- `+` : une addition de deux nombres
- `-` : une soustraction de deux nombres
- `*` : une multiplication de deux nombres
- `/` : une division de deux nombres

Tout autres caractères renverra une erreur.

**Flag** : `uhctf{C4lcul3s_3t_3xpr3ss10ns_M4gn1f1qu3s!}`

## Exemple d'utilisation :

```
$ nc {ip} {port}
Bienvenue sur le calculeur express !
Vous avez 1 minute pour résoudre un maximum de calculs !
5 ? 3 = 15
> *
2 ? 3 = 5
> +
4 ? 1 = 3
> -
18 ? 9 = 2
> /
```

## Code source :

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

#define MAX 100

#define MAX_OPERATIONS 100

#define OPERATORS "+-*/"

__attribute__((constructor)) void flush_buf() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}

char *read_line() {
    char *line = malloc(MAX);
    fgets(line, MAX, stdin);
    return line;
}

void print_flag() {
    FILE* flag_file;
    char c;

    flag_file = fopen("flag.txt", "r");

    if (flag_file != NULL) {
        while ((c = getc(flag_file)) != EOF) {
            printf("%c", c);
        }
        printf("\n");
    }
    else {
        printf("Could not find flag.txt\n");
    }
}

int is_operator(char c) {
    return strchr(OPERATORS, c) != NULL;
}

int is_digit(char c) {
    return c >= '0' && c <= '9';
}

int main() {
  size_t i;
  char *line;
  char *operations[MAX_OPERATIONS];
  char *token;
  char *saveptr;
  int nb_operations = 0;
  int result = 0;

  // Print welcome message
  printf("Bienvenue sur le calculeur express !\n");
  printf("Vous avez 1 minute pour résoudre un maximum de calculs !\n");

  for (i = 0; i < MAX_OPERATIONS; i++) {
    printf("> ");
    line = read_line();

    // Check if user wants to quit
    if (strcmp(line, "quit\n") == 0) {
      printf("Au revoir !\n");
      exit(0);
    }

    // Split line into tokens
    token = strtok_r(line, " ", &saveptr);
    while (token != NULL) {
      operations[nb_operations++] = token;
      token = strtok_r(NULL, " ", &saveptr);
    }

    // Check if user wants to submit
    if (strcmp(operations[0], "=") == 0) {
      break;
    }
  }
}
