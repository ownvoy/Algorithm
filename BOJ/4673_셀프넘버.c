#include <stdio.h>

int digit_count(int number)
{
    int i = 1;
    int count = 0;
    while (number / i != 0)
    {
        count += 1;
        i *= 10;
    }
    
    return count;
}

int divisor(int number)
{
    int i = 1;
    int divisor_max = 1;
    while (i <= number-1)
    {
        divisor_max *= 10;
        i++;
    }
    return divisor_max;
}

int main()
{
    int non_self_number[10000];
    for (int i = 1; i < 10000; i++)
    {
        int digit = digit_count(i);
        int Divisor = divisor(digit);
        non_self_number[i]= i ;
        int temp = i;
        while (Divisor >= 1)
        {
            int quoitent = temp / Divisor;
            temp -= quoitent * Divisor;
            non_self_number[i] += quoitent;
            Divisor /= 10;
        }

    }
    for (int i = 1; i < 10000; i++)
    {
        int zerocount = 0;
        for (int j = 1; j < 10000; j++){
        if (non_self_number[j] == i ){
            zerocount++;

            }
        }
        if (zerocount == 0){
            printf("%d\n", i);
        }
    }

    return 0;
}
    

