#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>


#define MAX 100
#define MIN 1

#define MAX_OPERATIONS 100

#define OPERATORS "+-*/"

__attribute__((constructor)) void flush_buf() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}

char get_random_operator() {
    return OPERATORS[rand() % strlen(OPERATORS)];
}

int get_random_number() {
    return rand() % (MAX - MIN + 1) + MIN;
}

char *get_random_operation() {
    char *operation = malloc(MAX);
    sprintf(operation, "%d %c %d", get_random_number(), get_random_operator(), get_random_number());
    return operation;
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

float exec_operation(int a, int b, char op) {
    switch (op) {
        case '+':
            return a + b;
        case '-':
            return a - b;
        case '*':
            return a * b;
        case '/':
            if (b == 0) {
                printf("Erreur: division par 0\n");
                exit(1);
            }
            return (float) a / b;
        default:
            printf("Erreur: '%c' n'est pas un opérateur valide\n", op);
            exit(1);
    }
}

int main() {
  // Initialize random seed
  srand(time(NULL));

  // Initialize variables
  size_t i;
  char *line;

  // Initialize timer
  time_t start;

  // Print welcome message
  printf("Bienvenue sur le calculeur express !\n");
  printf("Vous avez 1 minute pour résoudre un maximum de calculs !\n");
  printf("Le timer commence lorsque vous entrez votre première réponse.\n");

  for (i = 0; i < MAX_OPERATIONS; i++) {
    // Check if time is over
    if (i != 0 && time(NULL) - start > 60) {
      printf("Temps écoulé !\n");
      exit(0);
    }

    // Generate a random operation
    char operator = get_random_operator();
    int a = get_random_number();
    int b = get_random_number();

    float result = exec_operation(a, b, operator);

    printf("%d ? %d = %f\n", a, b, result);
    printf("> ");
    line = read_line();

    // Start timer
    if (i == 0) {
      start = time(NULL);
    }

    // Check if user wants to quit
    if (strcmp(line, "quit\n") == 0) {
      printf("Au revoir !\n");
      exit(0);
    }

    printf("check is operator %d\n", is_operator(line[0]));

    // Check if the line is an operator
    if (is_operator(line[0]) == 0) {
      printf("Erreur: '%c' n'est pas un opérateur valide\n", line[0]);
      exit(1);
      continue;
    }

    // Check if the operator from the line valid to use
    if (result != exec_operation(a, b, line[0])) {
      printf("Mauvaise réponse !\n");
      continue;
    }
  }

  print_flag();
}