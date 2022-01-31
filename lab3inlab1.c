#include<stdio.h>
void update(int*a,int*b)
{
    int x=*a+*b;
    int y=abs(*a-*b);
    *a=x;
    *b=y;
}
int main()
{
    int a, b;
    scanf("%d",&a);
    scanf("%d",&b);
    update(&a,&b);
    printf("%d\n",a);
    printf("%d\n",b);

    return 0;
}
