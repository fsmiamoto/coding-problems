#include <stdio.h>
#include <stdlib.h>

int cmp(const void *a, const void *b) { return *(int *)a - *(int *)b; }

int main() {
  int numOfLines;
  scanf("%d", &numOfLines);

  int *pares = (int *)malloc(numOfLines * sizeof(int));
  int *impares = (int *)malloc(numOfLines * sizeof(int));

  int lenPares = 0, lenImpares = 0;

  for (int i = 0; i < numOfLines; i++) {
    int n;
    scanf("%d", &n);
    if (n % 2 == 0) {
      pares[lenPares++] = n;
    } else {
      impares[lenImpares++] = n;
    }
  }

  qsort(pares, lenPares, sizeof(int), cmp);
  qsort(impares, lenImpares, sizeof(int), cmp);

  for (int i = 0; i < lenPares; i++) {
    printf("%d\n", pares[i]);
  }
  for (int i = lenImpares - 1; i >= 0; i--) {
    printf("%d\n", impares[i]);
  }

  free(pares);
  free(impares);
}
