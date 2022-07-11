from mimetypes import init
import sys
input = sys.stdin.readline
from collections import deque

sentence = deque(list(input().strip()))
sentence2 = deque([])
number = int(input())

commands = [input().strip().split() for _ in range(number)]

for command in commands:
    if command[0] == 'L':
        if(sentence):
            sentence2.appendleft(sentence.pop())
    elif command[0] == 'D':
        if(sentence2):
            sentence.append(sentence2.popleft())
    elif command[0] == 'B':
        if(sentence):
            sentence.pop()
        
    else:
            sentence.append(command[1])
print("".join(sentence + sentence2))



