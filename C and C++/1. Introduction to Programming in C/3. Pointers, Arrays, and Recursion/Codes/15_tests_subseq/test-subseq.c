#include <stdlib.h>
#include <stdio.h>

size_t maxSeq(int * array, size_t n);

int main() {
	int array1[] = {1, 2, 3, 2};
	int array2[] = {2, -3, 5, 6, 8};
	int array3[] = {5};
	int array4[] = {2, 4, 3, 6, 10, 15, -1, 7, 8, 2};
	int array5[] = {-2};
	int array6[] = {2,2,2,3};
	if (maxSeq(NULL, 0)) {
		printf("Failed on NULL\n");
		exit(EXIT_FAILURE);
	}
	if (maxSeq(array1, 0)) {
		printf("Failed on 1,2,3,2 for NULL\n");
		exit(EXIT_FAILURE);
	}
	if (maxSeq(array1, 4) != 3) {
		printf("Failed on 1,2,3,2\n");
		exit(EXIT_FAILURE);
	}
	if (maxSeq(array2, 5) != 4) {
		printf("Failed on 2,-3,5,6,8\n");
		exit(EXIT_FAILURE);
	}
	if (maxSeq(array3, 1) != 1) {
		printf("Failed on 5\n");
		exit(EXIT_FAILURE);
	}
	if (maxSeq(array4, 10) != 4) {
		printf("Failed on 2,4,3,6,10,15,-1,7,8,2\n");
		exit(EXIT_FAILURE);
	}
	if (maxSeq(array5, 1) != 1) {
		printf("Failed on -2\n");
		exit(EXIT_FAILURE);
	}
	if (maxSeq(array6, 4) != 2) {
		printf("Failed on 2,2,2,3\n");
		exit(EXIT_FAILURE);
	}
	return EXIT_SUCCESS;
}

// #include<stdio.h>

// #define EXIT_FAILURE 1;
// #define EXIT_SUCCESS 0;

// size_t maxSeq(int * array, size_t n);

// Write a function to do the test
// int doTest(int * array, int n, int y, int t) {
// if (maxSeq(array, n) != y) {
//  printf("Failed Test %d\n", t);
//  return EXIT_FAILURE;
// }
// else {
//  printf("Passed Test %d\n", t);
//  return EXIT_SUCCESS;
// }
// }

// int main() {
  // Defining arrays
  // int array1[] = {0};
  // int array2[] = {1, 6, 10, 1, -3, 4, 5, 10};
  // int array3[] = {};

  // Calling the test cases
  // doTest(array1, 2, 0, 1);
  // doTest(array1, 1, 2, 2);
  // doTest(array2, 8, 4, 3);
  // doTest(array3, 1, 0, 4);
//}
