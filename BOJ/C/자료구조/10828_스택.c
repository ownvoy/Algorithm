#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#define N 100000

int size(int stacks_size)
{
    if (stacks_size == 0)
    {
        printf("0\n");

        return 0;
    }
    printf("%d\n", stacks_size);

    return 0;
}

int empty(int stacks_size)
{
    if (stacks_size == 0)
    {
        printf("1\n");
    }
    else
    {
        printf("0\n");
    }
}

int pop(int *arr, int stacks_size)
{
    if (stacks_size == 0)
    {
        printf("-1\n");
        return 0;
    }

    printf("%d\n", arr[stacks_size - 1]);
    return 0;
}

int main()
{
    int number;
    int stacks_size = 0;
    int arr[N];
    char string[100];
    scanf("%d", &number);

    for (int i = 0; i < number; i++)
    {
        scanf("%s", string);
        if (strcmp(string, "size") == 0)
        {
            size(stacks_size);
        }

        if (strcmp(string, "empty") == 0)
        {
            empty(stacks_size);
        }

        if (strcmp(string, "push") == 0)
        {
            stacks_size++;
            scanf("%d", &arr[stacks_size - 1]);
        }

        if (strcmp(string, "pop") == 0)
        {
            pop(arr, stacks_size);
            if (stacks_size != 0)
            {
                stacks_size--;
            }
        }

        if (strcmp(string, "top") == 0)
        {
            pop(arr, stacks_size);
        }
    }
}
