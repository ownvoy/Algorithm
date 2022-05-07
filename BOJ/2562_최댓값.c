# include <stdio.h>

int main (){
    int i =0;
    int number[9]= {};
    int a = 0;

    for (i =0; i<=8; i++){    
        scanf("%d",&number[i]);
        
    }
    
    int max = number[0];
    int max_position = 1;
    for (i=0; i<=8; i++){
        if (number[i]<number[i+1]){
            max = number[i+1];
            max_position = i+2;
        }
    }

    printf("%d\n", max);
    printf("%d\n", max_position);
    
    return 0;

}