#include <stdio.h>
#include <stdlib.h>

typedef struct {
    unsigned int esq,dir;
} Par;

unsigned int menor(Par p);

int main()
{
    unsigned int num_botas;
    Par * pares;
    while(scanf("%u",&num_botas) != EOF)
    {
        unsigned int i, num_pares = 0;
        // Limites inferior e superior do vetor de pares
        unsigned int M = 30, m = 60;
        // Aloca vetor
        pares = (Par *) calloc(31,sizeof(Par));
        for(i = 0; i < num_botas; i++)
        {
            unsigned char pe;
            unsigned int tam;
            scanf("%u %c", &tam, &pe);
            // Tamanho 30 ocupa posicao 0 do vetor de pares
            unsigned int index = tam - 30;
            // Muda limites do vetor
            if(index > M)
                M = index;
            else if(index < m)
                m = index;
            // Contabiliza pe do par
            if(pe == 'E')
                pares[index].esq++;
            else
                pares[index].dir++;
        }
        // Soma o menor numero do par a num_pares
        for(i = m; i <= M; i++)
            num_pares += menor(pares[i]);
        // Saida do resultado
        printf("%u\n",num_pares);
    }
}

// Retorna o menor numero do par
unsigned int menor(Par p)
{
    if(p.dir < p.esq)
        return p.dir;
    return p.esq;
}
