#include <stdio.h>
#include <stdlib.h>

#define MAX 40

int main() {
  int n;
  int valores[MAX];

  scanf("%d", &n);

  int x = 0, y = 1, z;

  int pos = 0;
  do {
    valores[pos++] = y;
    z = x;
    x = y;
    y = z + y;
  } while (pos < n);

  for (int i = n - 1; i >= 0; i--) {
    printf("%d", valores[i]);
    if (i != 0) {
      printf(" ");
    }
  }

  printf("\n");
}
