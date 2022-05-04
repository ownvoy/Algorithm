# include <stdio.h>
#include <stdlib.h>

int maxfinder(int a[], int n){
    int max= a[0];
    
    for (int i=1;i<n;i++){
        if (a[i]> max){
            max = a[i];
        }
    }

    return max;
}

int minfinder(int a[], int n){
    int min= a[0];
    
    for (int i=1;i<n;i++){
        if (a[i]< min){
            min = a[i];
        }
    }

    return min;
}

int main(){
    int size;
    
    scanf("%d\n", &size);

    char str[100];
    char num[100];
    int arr[size];

    gets(str);
    int i=0;
    int o=0;
    int k=0;
    while(str[i] != '\0') {
        while(str[i]!=' ' && str[i] !='\0') {
            num[o]=str[i];
            o++;
            i++;
        }
        //아래는 띄어쓰기
        i++;
        o=0;
        arr[k] = atoi(num);
        k++;
    }

    int max = maxfinder(arr,size);
    int min = minfinder(arr,size);

    printf("%d %d\n", max, min);

    return 0;

}

