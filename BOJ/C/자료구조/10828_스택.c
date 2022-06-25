#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#define N 100000

typedef struct __Node
{
    int data;
    struct __Node *next;
} Node;

typedef struct __stack
{
    Node *head;
    int stacks_size;
} Stack;

void init(Stack *stack)
{
    stack->head = NULL;
    stack->stacks_size = 0;
}

void push(Stack *stack)
{
    Node *newnode = (Node *)malloc(sizeof(Node));

    scanf("%d", &newnode->data);
    newnode->next = stack->head;
    stack->head = newnode;
    stack->stacks_size++;
}

int pop(Stack *stack)
{
    if (stack->stacks_size == 0)
    {
        printf("-1\n");
        return 0;
    }

    printf("%d\n", stack->head->data);

    Node *Rnode = stack->head;
    int Rdata = Rnode->data;
    stack->head = Rnode->next;
    free(Rnode);
    stack->stacks_size--;

    return 0;
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

void empty(Stack *stack)
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

void top(Stack *stack)
{
    if (stack->stacks_size == 0)
    {
        printf("-1\n");
        return 0;
    }

    printf("%d\n", stack->head->data);
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
