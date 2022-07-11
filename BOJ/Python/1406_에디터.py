from mimetypes import init
import sys
input = sys.stdin.readline
from collections import deque


sentence = list(input().strip())
sentence2 = []
sentence_len = len(sentence)-1
number = int(input())
init_index = len(sentence)

commands = [input().strip().split() for _ in range(number)]

for command in commands:
    if command[0] == 'L':
        if(init_index == 0):
            continue
        init_index -= 1
    elif command[0] == 'D':
        if(init_index > sentence_len):
            continue
        init_index+=1
    elif command[0] == 'B':
        if(init_index == 0):
            continue
        sentence_len -= 1
        init_index -= 1
        sentence.pop(init_index)
        
    else:
        if(init_index > sentence_len):
            sentence.insert(init_index, command[1])
            init_index +=1
            sentence_len+=1
            continue
        sentence.insert(init_index, command[1])
        sentence_len+=1
        init_index +=1
sentence = "".join(sentence)
print(sentence)


