#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct stack
{
    int top;
    int data[100000];
} Stack;


void StackInit(Stack *stack)
{
    stack->top = -1;
}

int StackSize(Stack *stack)
{
    return (stack->top + 1);
}
void StackPush(Stack *stack, int value)
{
    stack->top++;
    stack->data[stack->top] = value;
}
int StackPop(Stack *stack)
{
    if (stack->top != -1)
    {
        int value = stack->data[stack->top];
        stack->top--;

        return value;
    }
    else
    {
        printf("Stack is empty\n");
        return 0;
    }
}

int main(){
    int number;
    scanf("%d", &number);
    Stack stack;
    StackInit(&stack);

    int array[number];
    int array_count[number];
    memset(array_count, 0, sizeof(array_count));
    
    char plus_minus[2 * number];
    int plus_minus_index = 0;
    int minus_count = 0;

    for(int i = 0; i < number; i++){ 
        scanf("%d", &array[i]);
    }
    while (minus_count < number)
    { // minus_count == number면 성공적으로 수행하고 끝남
        for (int i = 1; i <= array[minus_count]; i++)
        {
            if(array_count[i-1] == 0){
                StackPush(&stack, i);
                plus_minus[plus_minus_index++] = '+';
                array_count[i-1]++;//중복방지
            }
            else{
                array_count[i-1]++;
            }

        }
        if (array_count[array[minus_count] - 1] >= number)
        {// 5,3,4,1,2 같은 경우 한 바퀴 돌고, minus_count = 1인 상태에서 무한 루프 빠져서 처리해줌
        // i 대신에 array[minus_count]가 들어 간 것.
            break;
        }

        while(stack.data[stack.top] == array[minus_count] ){
            StackPop(&stack);

            plus_minus[plus_minus_index++] = '-';
            minus_count++;
            if(stack.top == -1){
                break;
            }
            

        }

    }

    if(minus_count!=number){
        printf("NO\n");
    }

    else{
        for(int i = 0; i < number*2; i++){
            printf("%c\n", plus_minus[i]);
        }
    }

    return 0;
}