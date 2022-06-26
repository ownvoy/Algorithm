#include <stdio.h>

int throw(int *arr, int size)
{

    while (size >= 4)
    {
        arr[size - 2] = arr[1];
        for (int i = 0; i <= size - 3; i++)
        {
            arr[i] = arr[i + 2];
        }
        size--;
    }
    printf("%d", arr[1]);
}

int main()
{
    int N;
    scanf("%d", &N);
    int arr[N];
    for (int i = 0; i < N; i++)
    {
        arr[i] = i + 1;
    }
    throw(arr, N);
}