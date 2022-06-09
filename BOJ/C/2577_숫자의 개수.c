# include <stdio.h>

int main(){

    int number[3] = {};

    for(int i=0;i<3;i++){

        scanf("%d",&number[i]);
    }

    int product = number[0]* number[1]* number[2];
    //printf("%d\n", product);

    int digit = 0;
    for (int i = 1; i<1000000000; i*=10){
        if (product/i != 0){

            digit+=1;
        }
    }
    //printf("digit: %d\n",digit);

    int divisior = 1;
    for (int i =0;i<digit-1;i++){
        divisior *= 10;
    }
    //printf("max_digit: %d\n",divisior);

    int count[10]={0};
    
    for (int i = divisior; i >=1; i /= 10){
        int number = product/i;
        count[number]+=1;
        product = product - number*i;
    }

    for (int i =0; i<10;i++){
        printf("%d\n",count[i]);
    }
    
    return 0;

}