# include <stdio.h>

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
    int array[size];
    

    for (int i=0;i<size;i++){
        scanf("%d ",&array[i]);
    }


    int max = maxfinder(array,size);
    int min = minfinder(array,size);

    printf("%d %d\n", max, min);

    return 0;

}

