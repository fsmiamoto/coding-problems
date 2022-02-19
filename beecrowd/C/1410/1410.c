#include <stdio.h>
#include <stdlib.h>

void troca(int* a, int *b);

int main()
{
    int a, d, menor_atk;
    int* def;
    while(1)
    {
        int i,j;
        scanf("%u %u",&a, &d);
        if(a == 0 && d == 0)
            break;
        def = (int*) malloc(d*sizeof(int));

        // Obtem o atacante mais proximo do gol
        scanf("%d",&menor_atk);
        for(i = 1; i < a; i++)
        {
            int atual;
            scanf("%d",&atual);
            if(atual < menor_atk)
                menor_atk = atual;
        }

        for(i = 0; i < d; i++)
            scanf("%d",&def[i]);

        // Obtem os dois menores valores
        for(i = 0; i < 2; i++)
        {
            int menor = i;
            for(j = i + 1; j < d; j++)
            {
                if(def[j] < def[menor])
                    menor = j;
            }
            if(menor != i)
                troca(&def[i],&def[menor]);
        }

        // Compara com o atacante mais proximo do gol com o penultimo defensor
        if(menor_atk < def[1])
            printf("Y\n");
        else
            printf("N\n");
    }
    return 0;
}

void troca(int* a, int *b)
{
    int aux = *a;
    *a = *b;
    *b = aux;
}

