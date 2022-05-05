#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
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
        i++;
        o=0;
        arr[k] = atoi(num);
        memset(num, 0, 100);
        k++;
    }
    for(i=0;i<size;i++){         //examine
        printf("%d ", arr[i]);
    }

    return 0;
}