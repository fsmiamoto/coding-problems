#include <stdio.h>

int main() {
  int hour, minutes;

  while (scanf("%d %d", &hour, &minutes) != EOF) {
    printf("%02d:%02d\n", hour / 30, minutes / 6);
  };
}
