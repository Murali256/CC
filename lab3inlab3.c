#include<stdio.h>
int updateVar(int *d)
{
    *d=(*d)+10; 
}
void main()
{
    int n,d;
    scanf("%d",&n);
    for(int i=0;i<n;i++)
    {
        scanf("%d",&d);
        updateVar(&d);
        printf("%d\n",d);
    }
}