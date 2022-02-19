#include <stdio.h>
#include <stdlib.h>

int main()
{
    while(1)
    {
        unsigned int i, n, m;
        unsigned int menor, maior, falsos = 0;
        unsigned char * bilhetes;
        // Leitura de n e m
        scanf("%u %u",&n,&m);
        // Condicao de parada
        if(n == 0 && m == 0)
            break;
        // Aloca vetor
        bilhetes = (unsigned char *) calloc(n + 1, sizeof(unsigned char));
        // Inicializa limites
        menor = n;
        maior = 0;
        for(i = 0; i < m; i++)
        {
            unsigned int atual;
            scanf("%u",&atual);
            // Se o bilhete tiver numero maior que n, automaticamente eh falso.
            if(atual > n)
            {
                falsos++;
                continue;
            }
            // Ajusta limites de leitura posterior
            if(atual > maior)
                maior = atual;
            else if(atual < menor)
                menor = atual;
            bilhetes[atual]++;
        }
        // Le vetor de bilhetes no limites estabelecidos
        for(i = menor; i <= maior; i++)
        {
            // Caso um bilhetes tenha sido usado mais de uma vez.
            if(bilhetes[i] > 1)
                falsos ++;
        }
        // Imprime resultado
        printf("%u\n",falsos);
    }
    return 0;
}
