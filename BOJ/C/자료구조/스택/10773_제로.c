#include <stdio.h>
#include <string.h>

int main()
{
    int number;
    int sum = 0;
    scanf("%d", &number);

    int money[number];
    memset(money, -1, sizeof(int) * number);
    int j = 0;

    for (int i = 0; i < number; i++)
    {
        scanf("%d", &money[j]);
        if (money[j] == 0)
        {
            int temp = j - 1;

            money[temp] = -1;
            money[j] = -1;
            j = temp - 1;
        }
        j++;
    }

    int h = 0;
    while (money[h] != -1)
    {
        sum += money[h];
        if (h == number - 1)
        {
            break;
        }
        h++;
    }
    printf("%d", sum);
}
