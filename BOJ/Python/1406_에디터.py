from mimetypes import init
import sys
input = sys.stdin.readline
from collections import deque


sentence = deque(list(input().strip()))
sentence2 = deque([])
sentence_len = len(sentence)-1
number = int(input())
init_index = len(sentence)

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
        if(init_index > sentence_len):
            sentence.append(command[1])
print("".join(sentence + sentence2))



