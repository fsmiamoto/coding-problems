#include <stdio.h>
#include <stdlib.h>

int main()
{
    unsigned short int vol, n_vol;
    unsigned short int * placas;
    // Enquanto nao ler EOF
    while(scanf("%hu %hu",&vol, &n_vol)!= EOF)
    {
        placas = calloc(vol,sizeof(unsigned short int));
        unsigned short int i, index;
        // Marca posicoes lidas com 1
        for(i = 0; i < n_vol; i++)
        {
            scanf("%hu", &index);
            placas[index - 1] = 1;
        }
        // Se todos voltaram
        if(vol == n_vol)
        {
            printf("*\n");
            continue;
        }
        // Imprime posicoes sem indicador
        for(i = 0; i < vol; i++)
            if(!placas[i])
                printf("%hu ",i+1);
        putchar('\n');
    }
    return 0;
}
