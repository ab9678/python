#include<stdio.h>
#include<stdlib.h>
# define N 5

int stack[N];
int address = -1;
int ifFull_empty(int stack[N]){
    if (address >= N-1){
        return 1;   //stackoverflow
    }else if (address==-1){
        return 2;   //stackunderflow
      
    }else{
        return 0;
    }
    
}
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


void peek(){

}
void display(){

}
int main(){
    int choice ;
    int exitstatus;

    do{
        printf("What do you want to perfotm\n1:push()\t2:pop()\t3:peek()\t4:Display()");
        scanf("%d",&choice);

        switch (choice)
        {
        case 1:
            push();                 //updates the stack
            break;
        case 2:
            printf("%d\n",pop());  //deletes element from stack generally top-most element not really,
            break;                  //popping means returning the top-most element and move the address to the next lower address, that way the original element becomes inaccessible
        case 3: peek();             // returns top-most element
            break;
        case 4: display();          //print the entire array from top to bottom/reverse order
            break;
        default:printf("Incorrect entry");
            break;
        }
        printf("Do you Want to exit?(0/1)");
        scanf("%d",&exitstatus);
    }while(exitstatus != 0);        // this is written to very if the user wants to exit, until then keep running
    

    for(int i =0 ; i<N ; i++){
        printf("%d\t",stack[i]);    //this is not needed after I write the display() function, display function will
                                    //do this 
    }
}
