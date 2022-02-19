#include <stdio.h>
#include <stdlib.h>

#define TAM 1001

int main()
{
    unsigned int n, i;
    scanf("%u",&n);
    for(i = 0; i < n; i++)
    {
        char* letras = (char*) calloc(26,sizeof(char));
        char * frase = (char*) calloc(TAM,sizeof(char));
        unsigned int j, usadas = 0;

        getchar();
        gets(frase);

        for(j = 0; j < TAM; j++)
        {
            char c = frase[j];
            if(c == '\0')
                break;
            if(c >= 'a' && c <= 'z')
            {
                if(letras[c - 'a'] == 0)
                {
                    letras[c - 'a'] = 1;
                    usadas++;
                }
            }
        }

        if(usadas < 13)
            printf("frase mal elaborada\n");
        else if(usadas < 26)
            printf("frase quase completa\n");
        else
            printf("frase completa\n");
    }
    return 0;
}
