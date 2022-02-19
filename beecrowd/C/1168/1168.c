#include <stdio.h>
#include <stdlib.h>

#define MAX 101

int main()
{
    unsigned int n, i;
    // Leitura do numero de casos teste
    scanf("%u",&n);
    fflush(stdin);
    for(i = 0; i < n; i++)
    {
        unsigned int j;
        unsigned long int total_leds = 0;
        // Aloca espaco para a string de leitura
        char * input = calloc(MAX,sizeof(char));
        scanf("%s",input);
        for(j = 0; j < MAX; j++)
        {
            // Interrompe iteracao caso chegue ao fim da string.
            if(input[j] == '\0')
                break;
            // Para cada caracter lido, soma a quantidade de LED's correspondente
            switch(input[j])
            {
            case '0':
            case '6':
            case '9':
                total_leds += 6;
                break;
            case '2':
            case '3':
            case '5':
                total_leds += 5;
                break;
            case '1':
                total_leds += 2;
                break;
            case '8':
                total_leds += 7;
                break;
            case '4':
                total_leds += 4;
                break;
            case '7':
                total_leds += 3;
                break;
            }
        }
        // Saida da resposta
        printf("%lu leds\n",total_leds);
    }
    return 0;
}
