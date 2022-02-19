#include <stdio.h>

int main()
{
    int i, n, s, menor_s;
    // Leitura do saldo e do num. de transacoes
    scanf("%d %d",&n,&s);
    // Inicializa variavel menor_s
    menor_s = s;
    for(i = 0; i < n; i++)
    {
        int t;
        scanf("%d",&t);
        s += t;
        if(s < menor_s)
            menor_s = s;
    }
    // Saida de dados
    printf("%d\n",menor_s);
    return 0;
}
