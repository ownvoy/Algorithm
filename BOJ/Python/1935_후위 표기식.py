
from collections import deque
import sys
input = sys.stdin.readline


number = int(input().strip())
expression =list(input().strip())
substitution = [int(input()) for _ in range(number)]

def numchange(x):
    if (65<=ord(x)<=90):
        asc = ord(x) -65
        return substitution[asc]
    else:
        return x
    
new = map(numchange, expression)

expression = deque(new)
stack = deque([])

while(expression):
    while(expression[0] != '*' and expression[0] !='+'and expression[0] != '-' and expression[0] != '/'):
            stack.appendleft(expression.popleft())
    temp2 = float(stack.popleft())
    temp1 = float(stack.popleft())
    calculate = expression.popleft()
    if calculate == '*':
        stack.appendleft(temp1*temp2)
    if calculate == '+':
        stack.appendleft(temp1+temp2)
    if calculate == '-':
        stack.appendleft(temp1-temp2)
    if calculate == '/':
        stack.appendleft(temp1/temp2)
        
    if (len(expression) == 0):
            print("%.2f" %stack.popleft())
    