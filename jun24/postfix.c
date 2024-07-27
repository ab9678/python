# include <stdio.h>
#include <stdlib.h>

# define N 5

int stack [N];
int address = -1;

void push(){
    int x;
    printf("Enter data: ");
    scanf("%d",&x);

    if (ifFull_empty(stack[N]) == 1){
        printf("Stackoverflow");    // should use display() here before exit so that atleast the remaining stack which was entered can be accessed
        exit(0);
    }else{
        address++;
        stack[address]=x;
    }


}
int pop(){

    if(ifFull_empty(stack[N])==2){
        printf("Stackunderflow");
        exit(0);
    }else{
        return stack[address];
        address--;
    }
}


int main(){

// Covert infix to postfix

 
    
}