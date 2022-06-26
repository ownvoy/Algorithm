#include <stdio.h>
#include <string.h>
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
    int queue_size;
} Queue;

void init(Queue *queue)
{
    Node *newnode = (Node *)malloc(sizeof(Node));
    newnode->data = 1;
    queue->front = newnode;
    queue->back = newnode;
    queue->queue_size = 1;
}

void set(Queue *queue, int Number)
{
    queue->queue_size = Number;
    int count = 2;
    while (count <= queue->queue_size)
    {
        Node *newnode = (Node *)malloc(sizeof(Node));
        newnode->data = count;
        queue->back->next = newnode;
        queue->back = newnode;
        count++;
    }
    queue->back->next = queue->front;
}

int pop(Queue *queue, int jump)
{
    Node *Rnode = queue->back;
    Node *beforeRnode = (Node *)malloc(sizeof(Node));
    for (int i = 0; i < jump; i++)
    {
        Rnode = Rnode->next;
        if (i == jump - 2)
        {
            beforeRnode = Rnode;
        }
    }
    queue->back = beforeRnode;
    queue->back->next = Rnode->next;
    // printf("%d", Rnode->data);
    int ddata = Rnode->data;
    free(Rnode);
    return ddata;
    // return Rnode->data 살아 있을까? ㄴㄴ 안됨
}

int main()
{
    int K, N;
    int delete_num = 0;
    scanf("%d %d", &N, &K);
    int arr[N];
    Queue queue;
    init(&queue);
    set(&queue, N);
    for (int i = 0; i < N; i++)
    {
        arr[i] = pop(&queue, K);
    }
    printf("<");
    for (int j = 0; j < N - 1; j++)
    {
        printf("%d, ", arr[j]);
    }
    printf("%d", arr[N - 1]);
    printf(">");
}
