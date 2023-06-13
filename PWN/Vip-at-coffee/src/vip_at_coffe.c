

int main(void)
{
  size_t res;
  char username[16];
  int money;

  // Init the username buffer
  memset(username, 0, 16);

  // Init the money
  money = 10;

  puts("Bienvenue à la caffette en ligne !");
  puts("Je vois que vous n'avez pas encore de compte ?");
  printf("Ton pseudo : ");
  fgets(username, 16, stdin);
  res = strcspn(username, "\n");
  username[res] = '\0';

  printf("Bienvenue %s !\n Par défaut tu as été crédité de %d€.\n", username, money);
  puts("Pour le moment nous n'acceptons aucun transfert d'argent vers un compte client.\n");
  puts("Cependant, à l'avenir, vous pourrez acheter un café VIP pour 1000€.\n");

  menu();
  return 0;
}

