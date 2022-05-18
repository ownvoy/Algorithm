#include <stdio.h>
int max_finder(int *array, int Size)
{
    int max = array[0];
    for (int i = 0; i <= Size - 2; i++)
    {
        if (array[i] < array[i + 1])
        {
            max = array[i + 1];
        }
    }

    return max;
}

double scam_mean(int *array, int Size, int max)
{

    double scam_score[Size];
    double array_double[Size];
    double scam_sum = 0;
    double max_double = max;

    for (int i = 0; i <= Size - 1; i++)
    {
        array_double[i] = array[i];
        // printf("%d 'th score: %f\n", i + 1, array_double[i]);
        scam_score[i] = array_double[i] / max_double * 100;

        // printf("scam_score[%d]= %f\n", i, scam_score[i]);
        scam_sum += scam_score[i];
    }

    double mean = scam_sum / Size;
    return mean;
}

int main()
{
    int size;
    scanf("%d", &size);
    int subject_score[size];

    for (int i = 0; i <= size - 1; i++)
    {
        scanf("%d", &subject_score[i]);
    }

    int max = max_finder(subject_score, size);
    // printf("max: %d\n",max);
    // printf("subject score: %d\n", subject_score[1]);
    double scam = scam_mean(subject_score, size, max);

    printf("%g", scam);
    return 0;
}
