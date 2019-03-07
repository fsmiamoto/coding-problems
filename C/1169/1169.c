#include <stdio.h>
#include <math.h>

int main()
{
    // Variaveis utilizadas
    unsigned int i, n;
    // Numero de testes
    scanf("%d",&n);
    for(i = 0; i < n; i++)
    {
        unsigned int num_casas;
        long double peso;
        // Entrada do numero de casas
        scanf("%u",&num_casas);
        peso = pow(2,num_casas) - 1; // PG de razao 2.
        peso /= 12000.0;
        printf("%lli kg\n",(long long int) peso);
    }
    return 0;
}
