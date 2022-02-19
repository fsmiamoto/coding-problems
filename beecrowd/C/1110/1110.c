#include <stdio.h>

int main()
{
    int monte[100];
    int n, i;
    int frente = 0, fim;
    while(1)
    {
        scanf("%d",&n);
        if(n == 0)
            break;
        fim = n - 1;
        frente = 0;
        printf("Discarded cards: ");
        for(i = 0; i < n; i++)
            monte[i] = i + 1;
        for(i = 1; i < n; i++)
        {
            printf("%d",monte[frente]);
            monte[++fim] = monte[frente+1];
            frente += 2;
            if(i != n - 1)
                printf(", ");
        }
        printf("\nRemaining card: %d\n",monte[frente]);
    }
    return 0;
}
