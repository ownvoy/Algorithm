#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#define N 100000

typedef struct __arrayStack
{
    int arr[N];
    int stacks_size;
} Stack;

int size(Stack *stack)
{
    if (stack->stacks_size == 0)
    {
        printf("0\n");

        return 0;
    }
    printf("%d\n", stack->stacks_size);

    return 0;
}

int empty(Stack *stack)
{
    if (stack->stacks_size == 0)
    {
        printf("1\n");
    }
    else
    {
        printf("0\n");
    }
}

int top(Stack *stack)
{
    if (stack->stacks_size == 0)
    {
        printf("-1\n");
        return 0;
    }

    printf("%d\n", stack->arr[(stack->stacks_size) - 1]);
}

int pop(Stack *stack)
{
    if (stack->stacks_size == 0)
    {
        printf("-1\n");
        return 0;
    }

    printf("%d\n", stack->arr[(stack->stacks_size) - 1]);

    if (stack->stacks_size != 0)
    {
        stack->stacks_size--;
    }
    return 0;
}

void init(Stack *stack)
{
    stack->stacks_size = 0;
}

void push(Stack *stack)
{
    stack->stacks_size++;
    scanf("%d", &stack->arr[stack->stacks_size - 1]);
}

int main()
{
    int number;
    scanf("%d", &number);
    Stack stack;
    init(&stack);

    char string[100];

    for (int i = 0; i < number; i++)
    {
        scanf("%s", string);
        if (strcmp(string, "size") == 0)
        {
            size(&stack);
        }

        if (strcmp(string, "empty") == 0)
        {
            empty(&stack);
        }

        if (strcmp(string, "push") == 0)
        {
            push(&stack);
        }

        if (strcmp(string, "pop") == 0)
        {
            pop(&stack);
        }

        if (strcmp(string, "top") == 0)
        {
            top(&stack);
        }
    }
}
