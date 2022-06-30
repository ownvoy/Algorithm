#include <stdio.h>

int main(){
    int N;
    scanf("%d",&N);
    int arr[N];
    int min=0;
    int minindex;
    int temp;
    int count = 0;
    for (int i=0; i<N; i++){
        scanf("%d",&arr[i]);
    }
    while(count < N-1){ 
        min = arr[count];
        for (int i = count; i <= N-1; i++)
        {
            
            if (min >= arr[i])
            {
                min = arr[i];
                minindex = i;
            }
        }

        temp = arr[count];
        arr[count] = min;
        arr[minindex] = temp;
        count++;
    }
    
    for (int i = 0; i < N; i++){
        printf("%d\n", arr[i]);
    }


}