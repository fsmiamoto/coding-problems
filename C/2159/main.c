#include <math.h>
#include <stdio.h>

int main() {
  double n;
  scanf("%lf", &n);
  double lower = n / logl(n);
  printf("%.1lf %.1f\n", lower, 1.25506 * lower);
}
