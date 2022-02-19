#include <stdio.h>
#include <stdlib.h>

int main()
{
    // Variaveis usadas
    unsigned int num_lesmas;
    unsigned int * vel_lesmas;
    // Enquanto nao ler EOF
    while(scanf("%u",&num_lesmas) != EOF)
    {
        unsigned int i, mais_veloz;
        // Aloca vetor com as velocidades
        vel_lesmas = (unsigned int *) malloc(num_lesmas*sizeof(unsigned int));
        // Inicializa mais_veloz
        mais_veloz = 1;
        // Preenche vetor
        for(i = 0; i < num_lesmas; i++)
        {
            scanf("%u",&vel_lesmas[i]);
            unsigned int classe = vel_lesmas[i]/10 + 1;
            if(classe > mais_veloz)
                mais_veloz = classe;
        }
        // Saida da resposta
        printf("%u\n",mais_veloz);
    }
    return 0;
}
