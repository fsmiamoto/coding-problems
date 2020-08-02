#include <stdio.h>

int main() {
  char *line = NULL;
  size_t len = 0;
  ssize_t read;

  // Read the first line
  int n;
  scanf("%d\n", &n);

  char freq[26];

  while ((read = getline(&line, &len, stdin)) != -1) {
    int i;

    for (i = 0; i < 26; i++) {
      freq[i] = 0;
    }

    for (i = 0; i < read; i++) {
      if (line[i] >= 'a' && line[i] <= 'z')
        freq[line[i] - 'a']++;
      else if (line[i] >= 'A' && line[i] <= 'Z')
        freq[line[i] - 'A']++;
    }

    int max = freq[0];
    for (i = 0; i < 26; i++) {
      if (freq[i] > max)
        max = freq[i];
    }

    for (i = 0; i < 26; i++) {
      if (freq[i] == max) {
        printf("%c", i + 'a');
      }
    }

    printf("\n");
  }
}
