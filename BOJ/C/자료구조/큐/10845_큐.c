#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct _Queue
{
    int queue_size;
    int arr[10000];
} Queue;

int size(Queue *queue)
{
    printf("%d\n", queue->queue_size);
}

int empty(Queue *queue)
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
    front_data = queue->arr[0];
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
    back_data = queue->arr[queue->queue_size - 1];
    printf("%d\n", back_data);
}

int push(Queue *queue)
{
    scanf("%d", &queue->arr[queue->queue_size]);
    queue->queue_size++;
}

int pop(Queue *queue)
{
    if (queue->queue_size == 0)
    {
        printf("-1\n");
        return 0;
    }

    printf("%d\n", queue->arr[0]);
    queue->queue_size--;

    for (int i = 0; i < queue->queue_size; i++)
    {
        queue->arr[i] = queue->arr[i + 1];
    }
}

int init(Queue *queue)
{
    queue->queue_size = 0;
    memset(queue->arr, 0, sizeof(int) * 10000);
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