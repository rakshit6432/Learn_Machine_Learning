#include <stdio.h>
#include <stdlib.h>

// Function prototype
unsigned power (unsigned x, unsigned y);

// Testing function
void do_test(unsigned x, unsigned y, unsigned ans) {
  if (power(x, y) != ans) {
    printf("Test Broken by: %d, %d\n", x, y);
    exit(EXIT_FAILURE);
  }
}

int main (void) {
  do_test(2, 3, 8);
  do_test(0, 0, 1);
  do_test(5, 0, 1);
  do_test(0, 5, 0);
  do_test(1, 0, 1);
  do_test(2*3, 2, 36);
  do_test(2, 10, 1024);
  do_test(10, 2, 100);
  do_test(10, 5, 100000);
  return EXIT_SUCCESS;
}
