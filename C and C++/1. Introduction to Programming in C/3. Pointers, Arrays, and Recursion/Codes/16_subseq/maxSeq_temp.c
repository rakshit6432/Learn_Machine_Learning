#include<stdio.h>
#include<stdlib.h>


size_t maxSeq(int *array, size_t n) {
  // Create int variable to store the length of array
  int max, len;
  
  // If empty lis, then return NULL
  if (n==0) {max = 0;}
  else if (n==1) {max = 1;}
  else {
    // Iterate through the array
    for (int i=1; i<n-1; i++) {
      if (array[i] > array[i-1]) {
	len++;
      }
      else {
	if (max < len) {
	  max = len;
	}
	len = 1;
      }
    }
    if (max < len) {
      max = len;
    }
  }
  return max;
}
