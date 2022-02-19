#include <stdio.h>
#include <stdlib.h>

int main()
{
    unsigned short int n,i,index = 0;
    int * x;
    // Entrada do num de elementos
    scanf("%hu",&n);
    // Aloca vetor
    x = (int *) malloc(n*sizeof(int));
    // Preenche vetor verificando se o numero inserido eh menor
    for(i = 0; i < n; i++)
    {
        scanf("%d",&x[i]);
        if(x[i] < x[index])
            index = i;
    }
    // Saida de dados
    printf("Menor valor: %d\n",x[index]);
    printf("Posicao: %hu\n",index);
    return 0;
}
