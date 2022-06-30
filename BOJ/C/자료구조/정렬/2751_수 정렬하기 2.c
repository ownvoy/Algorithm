#include <stdio.h>
#include <stdlib.h>

void MergeTwoArea(int arr[], int left, int mid, int right)
{
    int firstindex1 = left;
    int firstindex2 = mid + 1;
    int *sortArr = (int *)malloc(sizeof(int) * (right + 1));
    int sortindex = left;

    while (firstindex1 <= mid && firstindex2 <= right)
    {
        if (arr[firstindex1] <= arr[firstindex2])
        {
            sortArr[sortindex] = arr[firstindex1];
            firstindex1++;
        }
        else
        {
            sortArr[sortindex] = arr[firstindex2];
            firstindex2++;
        }

        sortindex++;
    }

    if (firstindex1 > mid)
    {
        for (int i = firstindex2; i <= right; i++, sortindex++)
        {
            sortArr[sortindex] = arr[i];
        }
    }
    else
    {
        for (int i = firstindex1; i <= mid; i++, sortindex++)
        {
            sortArr[sortindex] = arr[i];
        }
    }

    for (int i = left; i <= right; i++)
    {
        arr[i] = sortArr[i];
    }

    free(sortArr);
}

void MergeSort(int arr[], int left, int right)
{
    int mid;

    if (left < right)
    {
        mid = (left + right) / 2;

        MergeSort(arr, left, mid);
        MergeSort(arr, mid + 1, right);

        MergeTwoArea(arr, left, mid, right);
    }
}

int main(void)
{
    int N;
    scanf("%d", &N);
    int arr[N];
    for (int i = 0; i < N; i++)
    {
        scanf("%d", &arr[i]);
    }
    MergeSort(arr, 0, N - 1);

    for (int i = 0; i < N; i++)
    {
        printf("%d\n", arr[i]);
    }
    return 0;
}