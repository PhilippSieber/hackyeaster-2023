#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <math.h>

#define BUFSIZE 5
#define ptr_index BUFSIZE
#define result_index (BUFSIZE + 1)

void read_ints(long long *input, int total) {
  // off by one error :)
  for (int i = 0; i <= total; ++i) {
    if (scanf("%lld", &input[i]) != 1 ) {
      exit(-1);
    }

    if (!input[i]) {
      break;
    }
  }
}

int norm(long long *input, long long *result) {
  *result = 0;
  int i = 0;

  while (input[i] != 0) {
    *result += input[i];
    i++;
  }

  *result /= i;

  return i;
}

static void setup(void) __attribute__((constructor));

void setup() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    alarm(30);
}

// there's no pop rdi; ret gadget in the binary otherwise which is needed to execute syscalls
void probably_helpful_gadget() {
   __asm__ volatile ("pop %rdi");
   __asm__ volatile ("ret");
}

void main() {
  // user input, pointer to the result, result
  long long input[BUFSIZE + 2] = { 0 };
  input[ptr_index] = (long long) &input[result_index];

  printf("Give me a list of integers and I calculate the average\n");
  printf("0 is interpreted as the end of the input\n");

  read_ints(input, BUFSIZE);

  if (norm(input, (long long *) input[ptr_index]) > BUFSIZE ) {
    exit(-1);
  }

  printf("%lld\n", input[result_index]);
}

