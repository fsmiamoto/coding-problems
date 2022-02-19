#include <stdio.h>
#include <stdlib.h>

#define X_MAX 2000

int main()
{
    unsigned int n, i;
    unsigned int menor = X_MAX, maior = 0;
    // Aloca vetor ja zerado com X_MAx + 1 posicoes para simplificar indices
    unsigned int * freq = calloc(X_MAX + 1,sizeof(unsigned int));;
    scanf("%u",&n);
    for(i = 0; i < n; i++)
    {
        unsigned int atual;
        scanf("%u",&atual);
        // Ajusta limites de leitura do vetor
        if(atual > maior)
            maior = atual;
        else if(atual < menor)
            menor = atual;
        // Adiciona 1 na posicao correspondente no vetor freq
        freq[atual]++;
    }
    for(i = menor; i <= maior; i++)
        // Imprime frequencia para elementos que apareceram
        if(freq[i] != 0)
            printf("%u aparece %u vez(es)\n",i,freq[i]);
    return 0;
}
