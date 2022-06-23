#include <stdio.h>
#define MAX_STR_SIZE 100

int main()
{
    char str_read[MAX_STR_SIZE];
    fgets(str_read, MAX_STR_SIZE, stdin);
    printf("output: %s \n", str_read);
    printf("%c\n", str_read[0]);
    printf("%c\n", str_read[1]);
    printf("%c\n", str_read[2]);

    return 0;
}
