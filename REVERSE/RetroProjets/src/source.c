#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdarg.h>


__attribute__((constructor)) void flush_buf() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}

bool is_printable( char c )
{
    return !( c & (1 << 7) );
}

void c(char *buf, ...)
{
	va_list args;
	va_start (args, buf);     /* Initialize the argument args. */

	char arg = va_arg(args, int);
	
	while( arg ) {
		sprintf(buf, "%s%c", buf, arg);
		arg = va_arg(args, int);
	}

	va_end (args);                  /* Clean up. */
}

char* encrypt(char *str) {
    char current;
    int i;

    for (i = 0; i < strlen(str); i++) {
        current = str[i];
        if (isalpha(current)) {
            if (isupper(current)) {
                current = ((current - 'A') + 13) % 26 + 'A';
            } else {
                current = ((current - 'a') + 13) % 26 + 'a';
            }
        }
        str[i] = current;
    }

    return str;
}

int main(void)
{
  int result;
  char* enc;
  char input[33];

  char FLAG[33];
  c(FLAG, 'H', 'U', 'B', 'P', 'G', 'S', '{', 'V', 'a', 'f', 'c', 'v', 'e', 'n', 'g', 'v', 'b', 'a', '_', 'S', 'e', 'b', 'z', '_', 'G', 'u', 'r', '_', 'C', 'n', 'f', 'g', '}');

  printf("Tu souhaite accéder aux projets ?\n");
  puts("Entrez le mot de passe :");
  fgets(input, sizeof(input), stdin);
  enc = encrypt(input);
  result = strcmp(enc, FLAG);
  if (result == 0) {
    printf("Voici la liste des projets :\n");
    printf("1. RetroProjets\n");
    printf("2. RetroProjets2\n");
    printf("3. RetroProjets3\n");
    printf("4. RetroProjets4\n");
    printf("5. RetroProjets5\n");
  }
  else {
    printf("Mauvais mot de passe !\n");
  }

  return 0;
}