#include <stdio.h>

int main()
{
    
    int number;
    scanf("%d", &number);

    while (number != 0)
    {
        
        
        int i = 10000;
        int digit_number = 5;
        while (i > 0)
        {
            if (number / i == 0)
            {
                digit_number--;
                i /= 10;
            }
            else
            {
                int arr[digit_number];
                for (int j = 0; j < digit_number; j++){
                    arr[j] = number / i;
                    number -= i * (number / i);
                    i /= 10;
                }
                int errorcount = 0;
                for (int k = 0; k < digit_number / 2; k++)
                {
                    if(arr[k] != arr[digit_number - k-1]){
                        errorcount++;
                    }
                }
                i = 0;
                if(errorcount == 0){
                    printf("yes\n");
                }
                else{
                    printf("no\n");
                }

            }
        }
        scanf("%d", &number);
    }
}