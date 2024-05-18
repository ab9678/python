# include<stdio.h>


int main(){

int array1[] = {0,1,1,3,3,5,6};

int i,j;
for (i=0;i<7;i++){
    for (j=i+1;j<7;j++){
        if (array1[i]==array1[j]){
            printf("%d",array1[i]);
        }

    }
}


}