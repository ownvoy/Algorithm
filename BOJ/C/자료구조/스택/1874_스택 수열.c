#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct stack
{
    int top;
    int data[100000];
} Stack;

Stack stack;

void StackInit()
{
    stack.top = -1;
}

int StackSize()
{
    return (stack.top + 1);
}
void StackPush(int value)
{
    stack.top++;
    stack.data[stack.top] = value;
}
int StackPop()
{
    if (stack.top != -1)
    {
        int value = stack.data[stack.top];
        stack.top--;

        return value;
    }
    else
    {
        printf("Stack is empty\n");
        return 0;
    }
}

int main()
{
    int number;
    scanf("%d", &number);
    StackInit();

    int target;

    char plus_minus[2 * number];
    int char_index = 0;
    int plus = 1; //오름차순으로 시작

    for (int i = 0; i < number; i++)
    {
        scanf("%d", &target);
        while (target >= plus)
        {
            StackPush(plus);
            plus++;
            plus_minus[char_index++] = '+';
        }
        if (target == StackPop())
        {
            plus_minus[char_index++] = '-';
        }

        else
        {
            printf("NO");
            return 0;
        }
    }

    for (int i = 0; i < number * 2; i++)
    {
        printf("%c\n", plus_minus[i]);
    }
    return 0;
}