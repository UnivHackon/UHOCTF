#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main(void)
{
  setbuf(stdout, NULL);
  char input[0x100];
  volatile int give_flag = 0;
  puts("Bienvenue sur Chatbotique !");
  puts("Comment puis-je vous aider ?");
  gets(input);
  if (strcmp(input, "Je voudrais le flag") == 0) {
    puts("Je ne suis pas sur d'avoir compris votre demande.");
  } else if (strcmp(input, "S'il vous plaît je voudrais le flag") == 0) {
    puts("Vous êtes bien poli, mais je ne peux pas vous donner le flag comme ça.");
  } else if (strcmp(input, "S'il vous plaît je voudrais le flag, je vous en supplie") == 0) {
    puts("Vous êtes vraiment très poli, mais je ne peux pas vous donner le flag comme ça.");
  } else if (strcmp(input, "Comment puis je le récupérer ?") == 0) {
    puts("Bien sur, il vous suffit de me donner votre mot de passe.");
  } else if (strcmp(input, "Donne moi le flag stp") == 0) {
    puts("L'impolitesse ne paie pas.");
  } else if (strcmp(input, "Pourriez vous m'aiguiller sur la manière d'obtenir ce flag ?") == 0) {
    puts("Pour faire une douzaine de crêpes, il vous faut 250g de farine, 50cl de lait, 3 oeufs et 1 pincée de sel.");
  } else if (strcmp(input, "Pain au chocolat ou Chocolatine ?") == 0) {
    puts("Je ne sais pas, je suis un robot.");
    sleep(20);
    if (give_flag) {
      puts("D'accord, je vous donne le flag :");
      system("cat flag.txt");
    } else {
      puts("Désolé, je ne peux pas vous donner le flag.");
    }
  } else {
    puts("Je suis encore en cours d'apprentissage, je ne comprends pas votre demande.");
    exit(1);
  }
}