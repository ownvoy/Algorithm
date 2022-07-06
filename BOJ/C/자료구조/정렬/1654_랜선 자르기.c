#include <stdio.h>

long int min(long int *arr, int K)
{
    long int min = arr[0];
    int minindex = 0;
    for (int i = 0; i < K; i++)
    {
        if (min > arr[i])
        {
            min = arr[i];
            minindex = i;
        }
    }
    return min;
}

int maxindex(long int *arr, int K)
{
    long int max = arr[0];
    int maxindex = 0;
    for (int i = 0; i < K; i++)
    {
        if (max < arr[i])
        {
            maxindex = i;
            max = arr[i];
        }
    }
    return maxindex;
}

int main()
{
    int N;
    int K;
    scanf("%d %d", &K, &N);
    long int num[K];
    long int sum = 0;

    for (int i = 0; i < K; i++)
    {
        scanf("%ld", &num[i]);
        sum += num[i];
    }

    long int mean = sum / N;
    int count = 0;
    long int many[K];
    long int remainder[K];
    if (mean > min(num, K))
    {
        printf("%d", min(num, K));
        return 0;
    }

    for (int i = 0; i < K; i++)
    {
        many[i] = num[i] / mean;
        remainder[i] = num[i] % mean;
        count += many[i];
    }

    while (count != N)
    {
        int maxRemainderIndex = maxindex(remainder, K);
        remainder[maxRemainderIndex] -= mean;
        many[maxRemainderIndex]++;
        count++;
    }

    long int quoitent[K];
    for (int i = 0; i < K; i++)
    {
        quoitent[i] = num[i] / many[i];
    }

    long int maxlength = min(quoitent, K);
    printf("%ld", maxlength);
}
