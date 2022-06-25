#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct _node
{
    int data;
    struct _node *next;
} Node;

typedef struct _Queue
{
    Node *front;
    Node *back;
    int queue_size;
} Queue;

void init(Queue *queue)
{
    queue->front = NULL;
    queue->back = NULL;
    queue->queue_size = 0;
}

int push(Queue *queue)
{
    Node *newnode = (Node *)malloc(sizeof(Node));
    scanf("%d", &newnode->data);
    if (queue->queue_size == 0)
    {
        queue->front = newnode;
        queue->back = newnode;
        queue->queue_size++;

        return 0;
    }
    queue->back->next = newnode;
    queue->back = newnode;
    queue->queue_size++;
}

void size(Queue *queue)
{
    printf("%d\n", queue->queue_size);
}

void empty(Queue *queue)
{
    if (queue->queue_size == 0)
    {
        printf("1\n");
    }
    else
    {
        printf("0\n");
    }
}

int front(Queue *queue)
{
    if (queue->queue_size == 0)
    {
        printf("-1\n");
        return 0;
    }

    int front_data;
    front_data = queue->front->data;
    printf("%d\n", front_data);
}

int back(Queue *queue)
{
    if (queue->queue_size == 0)
    {
        printf("-1\n");
        return 0;
    }

    int back_data;
    back_data = queue->back->data;
    printf("%d\n", back_data);
}

int pop(Queue *queue)
{
    if (queue->queue_size == 0)
    {
        printf("-1\n");
        return 0;
    }
    Node *Rnode = queue->front;
    queue->front = queue->front->next;
    printf("%d\n", Rnode->data);
    free(Rnode);
    queue->queue_size--;
}

int main()
{
    int command_number;
    scanf("%d", &command_number);
    char string[100];
    Queue queue;
    init(&queue);

    for (int i = 0; i < command_number; i++)
    {
        scanf("%s", string);

        if (strcmp(string, "size") == 0)
        {
            size(&queue);
        }

        if (strcmp(string, "empty") == 0)
        {
            empty(&queue);
        }

        if (strcmp(string, "push") == 0)
        {
            push(&queue);
        }

        if (strcmp(string, "pop") == 0)
        {
            pop(&queue);
        }
        if (strcmp(string, "front") == 0)
        {
            front(&queue);
        }
        if (strcmp(string, "back") == 0)
        {
            back(&queue);
        }
    }
}