#include <stdio.h>
#include <stdlib.h>

typedef struct _NODE
{
    int data;
    struct _NODE *next;
} Node;

typedef struct _Queue
{
    Node *front;
    Node *back;
    int size;
} Queue;

int init(Queue *queue)
{
    Node *newnode = (Node *)malloc(sizeof(Node));
    newnode->data = 1;
    queue->front = newnode;
    queue->back = newnode;
    queue->size = 1;
}

int set(Queue *queue, int size)
{
    queue->size = size;
    for (int i = 2; i <= size; i++)
    {
        Node *newnode = (Node *)malloc(sizeof(Node));
        newnode->data = i;
        queue->back->next = newnode;
        queue->back = newnode;
    }
}

int pop(Queue *queue)
{

    while (queue->size > 4)
    {
        Node *Rnode = (Node *)malloc(sizeof(Node));
        Node *Mnode = (Node *)malloc(sizeof(Node));
        Node *Tempnode = (Node *)malloc(sizeof(Node));

        Rnode = queue->front;
        Mnode = queue->front->next;
        queue->front = Mnode->next;
        free(Rnode);
        Tempnode = Mnode;
        queue->back->next = Tempnode;
        queue->back = Tempnode;
        free(Mnode);
        queue->size--;
    }
    if (queue->size == 4)
    {
        printf("%d", queue->back->data);
    }
    if (queue->size == 3)
    {
        printf("%d", queue->front->next->data);
    }
    if (queue->size == 2)
    {
        printf("%d", queue->back->data);
    }
    if (queue->size == 1)
    {
        printf("%d", queue->front->data);
    }
}

int main()
{
    int number;
    scanf("%d", &number);
    Queue queue;
    init(&queue);
    set(&queue, number);
    pop(&queue);
}
