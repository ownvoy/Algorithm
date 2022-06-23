#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#define N 100000

typedef struct __stackNode{
    int data;
    int stacks_size;
    struct __stackNode *next;
} Stack;


void init(Stack *stack ){
    stack -> next = NULL;
    stack -> stacks_size = 0;
}

void push(Stack *stack){
    Stack *newNode = (Stack *)malloc(sizeof(Stack));

    scanf("%d", &newNode->data);
    stack -> next = newNode;

}

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

    printf("%d\n", stack->data);
}

int pop(Stack *stack)
{
    if (stack->stacks_size == 0)
    {
        printf("-1\n");
        return 0;
    }

    printf("%d\n", stack->data);

    int Rdata = stack->data;
    Stack Rstack = stack->next;
    
    if (stack->stacks_size != 0)
    {
        stack->stacks_size--;
    }
    return 0;
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
