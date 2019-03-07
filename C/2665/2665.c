#include <stdio.h>
#include <stdlib.h>

int main()
{
	int n, i, topo, carta;
	int * monte;
	long long int soma;
	while(scanf("%d",&n) != EOF)
	{

		monte[0] = 0;
		soma = 0;
		topo = 0;
		for(i = 0; i < n; i++)
		{
			scanf("%d",&carta);
			while(monte[topo] > carta)
				soma += monte[topo--];
			monte[++topo] = carta;
		}
		printf("%lli\n",soma);
		free(monte);
	}
	return 0;
}
