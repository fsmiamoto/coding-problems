#include <stdio.h>

int main()
{
    unsigned int i, n, cap_max;
    unsigned int atual = 0, excedeu = 0;
    // Leitura dos testes e da cap. maxima
    scanf("%u %u",&n,&cap_max);
    for(i = 0; i < n; i++)
    {
        unsigned int in, out;
        scanf("%u %u",&out, &in);
        atual += in - out;
        if(atual > cap_max)
            excedeu = 1;
    }
    // Se excedeu...
    if(excedeu)
        printf("S\n");
    else
        printf("N\n");
    return 0;
}
