#include <stdio.h>

long long sum_finder(int* a, int n){
    long long integer_sum = 0;
    for (int i = 0; i < n; i++)
    {
        integer_sum += a[i];
    }

    return integer_sum;
}

int main(){
    int number;
    scanf("%d", &number);
    int number_arr[number];
    for (int x = 0; x < number; x++){

        scanf("%d", &number_arr[x]);
    }

    int finalsum;
    int sum = sum_finder(number_arr, number);
    printf("%ld",sum);
    return 0;
}
