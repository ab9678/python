#include<stdio.h>
int main(){
    int element;
    scanf ("%d",&element);

    switch (element)
    {
    case 2:
        printf("hello");
        break;
    case 10:
        printf("nope");
        break;
    default:
        printf("No heloo");
        break;
    } 
}