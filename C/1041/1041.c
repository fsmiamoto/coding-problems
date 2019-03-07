#include <stdio.h>

int main()
{
    float a,b;
    scanf("%f %f",&a,&b);
    if(a*b > 0)
    {
        if(a < 0)
            puts("Q3");
        else
            puts("Q1");
    }
    else if(a*b < 0)
    {
        if(a < 0)
            puts("Q2");
        else
            puts("Q4");
    }
    else
    {
        if(a != 0)
            puts("Eixo X");
        else if(b != 0)
        {
            puts("Eixo Y");
        }
        else
            puts("Origem");
    }
    return 0;
}
