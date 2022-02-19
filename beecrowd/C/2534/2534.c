#include <stdio.h>

void quick_sort(int *a, int left, int right);

int main()
{
    int n, q, i, p;
    while(scanf("%d %d",&n,&q)!= EOF)
    {
        int notas[n];

        // Le notas
        for(i = 0; i < n; i++)
            scanf("%d",&notas[i]);

        // Ordena vetor de notas
        quick_sort(notas,0,n-1);

        // Imprime nota da posicao correspondente
        for(i = 0; i < q; i++)
        {
            scanf("%d",&p);
            printf("%d\n",notas[n-p]);
        }
    }
    return 0;
}

void quick_sort(int *a, int left, int right)
{
    int i, j, x, y;

    i = left;
    j = right;
    x = a[(left + right) / 2];

    while(i <= j)
    {
        while(a[i] < x && i < right)
        {
            i++;
        }
        while(a[j] > x && j > left)
        {
            j--;
        }
        if(i <= j)
        {
            y = a[i];
            a[i] = a[j];
            a[j] = y;
            i++;
            j--;
        }
    }

    if(j > left)
    {
        quick_sort(a, left, j);
    }
    if(i < right)
    {
        quick_sort(a, i, right);
    }
}
