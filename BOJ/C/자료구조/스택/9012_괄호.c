#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct __Node
{
    int data;
    struct __Node *next;
} Node;

typedef struct __stack
{
    Node *head;
    int check;
} Stack;

void init(Stack *stack)
{
    stack->head = NULL;
    stack->check = 0;
}

void push(Stack *stack, char character)
{
    Node *newnode = (Node *)malloc(sizeof(Node));

    newnode->data = character;
    newnode->next = stack->head;
    stack->head = newnode;
}

int parenthesis(Stack *stack, int stringlen)
{

    Node *R1node = stack->head;

    if (R1node->data == ')') // 첫번째가 ')'로 시작하면 안됨
    {
        stack->check++;
    }

    else
    {
        Node *R2node = R1node->next;
        int R2data = R2node->data;
        Node *beforeR2node;

        int repeat = 0;

        if (R2data == ')')
        {
            stack->head = R2node->next;
            free(R2node);
            free(R1node);

            return 0;
        }

        while (R2data != ')') // ')'가 나올 때까지 옆 노드 이동
        {
            beforeR2node = R2node;
            R2node = R2node->next;
            if (R2node == NULL)
            {
                stack->check++;
                return 0;
            }
            R2data = R2node->data;
            repeat++;

            // if(repeat > stringlen){
            //     stack->check++;

            //     break;
            // }
        }

        beforeR2node->next = R2node->next;
        stack->head = R1node->next;
        free(R1node);
        free(R2node);
    }
}

void checking(Stack *stack)
{
    if (stack->check > 0)
    {
        printf("NO\n");
        // printf("errorcount: %d\n", stack->check);
    }
    else
    {
        printf("YES\n");
    }
}

int main()
{
    int testcase;
    scanf("%d", &testcase);
    char string[100];
    Stack stack;
    // Stack *stack 으로 하면 안됨

    for (int i = 0; i < testcase; i++)
    {
        init(&stack);
        scanf("%s", string);
        int stringlen = strlen(string);
        if (stringlen % 2 != 0)
        {
            printf("NO\n");
            continue;
        }
        for (int j = stringlen - 1; j >= 0; j--)
        {
            push(&stack, string[j]);
        }
        int pnumber = stringlen / 2;

        for (int h = 0; h < pnumber; h++)
        {
            parenthesis(&stack, stringlen);
        }
        checking(&stack);
    }
}
