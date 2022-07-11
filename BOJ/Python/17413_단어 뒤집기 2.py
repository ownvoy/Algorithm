import sys
input = sys.stdin.readline
from collections import deque

sentence =list(input().strip().replace("<", "_<").replace(">", ">_").replace(" ", "_*_").split("_"))
status = 0
for word in sentence:
    if(word):
        if(word[0]== '<'):
            status = 1
        if( status ==0):
            word = word[::-1]
            print(word.replace("*", " "), end ="")
        elif(status ==1):
            modi = deque(list(word))
            last_char = modi.pop()
            if(last_char=='>'):
                modi.append(last_char)
                print("".join(list(modi)).replace("*", " "), end="")
                status = 0
            else:
                modi.append(last_char)
                print("".join(list(modi)).replace("*", " "), end="")
                
    else:
        print(word, end="")
