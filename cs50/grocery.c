# include <stdio.h>

typedef struct grocery{
    int count;
    char firstLetter;
}item;

int main(){
    item a[9];
    
    char letter;
    int i=-1,k=0;
    int j=0;
    for (i=0;i<9;i++){
        a[i].count = 1;
    }
     i = 0;
    while(i<9-1){
        int flag = 0;
        printf("item: ");
        scanf(" %c",&letter);
        
        if (letter == '|'){
            break;
        }else{
            for (j=0;j<9;j++){
                if (a[j].firstLetter == letter ){
                    a[j].count++;
                    int flag = 1;
                    break;
                }
            }
            if (flag != 1){
                i++;
                a[i].firstLetter = letter;
                a[i].count = 1;
                
            }
        } 

        

    }
    k=i;

    for (i=0;i<k;i++){
        printf(" %c\t",a[i].firstLetter);
        printf("%d",a[i].count);
        printf("\n");
    }

}