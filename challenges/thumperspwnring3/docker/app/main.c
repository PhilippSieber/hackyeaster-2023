#include <stdlib.h>
#include <stdio.h>
#include <string.h>

void main() {
  // Disable buffering
  setbuf(stdout, NULL);
  setbuf(stdin, NULL);

  printf("Welcome to the password protected vault\n");
  printf("Please enter your password: ");

  char input[256]; 
  // need to add the newline explicitly so it matches what we get from fgets
  char* password = "5uP3R_s3cUr3_PW\n";
  fgets(input, sizeof(input), stdin);

  if (strcmp(password, input) == 0) {
    system("cat /challenge/FLAG");
  } else {
    printf("Nope..\n");
    printf(input);
    printf("is incorrect. Better luck next time\n");
  }
}
