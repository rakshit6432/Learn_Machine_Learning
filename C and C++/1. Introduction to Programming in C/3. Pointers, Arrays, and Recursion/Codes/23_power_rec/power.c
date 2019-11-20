#include <stdio.h>
#include <stdlib.h>

unsigned power(unsigned x, unsigned y) {
  // For 0, 0 input
  if ((x == 0 && y == 0) || (x>0 && y==0)) {
    return 1;
  }
  if (x == 0 && y>0) {
    return 0;
  }
  if (y == 1) {
    return x;
  }
  return x*(power(x, y-1));
}
