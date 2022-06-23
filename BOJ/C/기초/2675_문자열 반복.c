#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct _test
{
    int repeat;
    char string[];
} test;

int main()
{
    int testcase;
    scanf("%d", &testcase);

    for (int i = 0; i < testcase; i++)
    {
        test ap;

        scanf("%d", &ap.repeat);
        scanf("%s", ap.string);
        int stringlen = strlen(ap.string);
        if (stringlen > 0)
        {
            char *newstrptr = (char *)malloc(sizeof(char) * (stringlen));
            strcpy(newstrptr, ap.string);

            for (int j = 0; j < sizeof(newstrptr) / sizeof(char); j++)
            {
                for (int h = 0; h < ap.repeat; h++)
                {
                    printf("%c", newstrptr[j]);
                }
            }
            free(newstrptr);
        }
        printf("\n");
    }

    return 0;
}
