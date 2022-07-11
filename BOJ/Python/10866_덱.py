from collections import deque
import sys
input = sys.stdin.readline

N = int(input().strip())
numdeque = deque([])

for _ in range(N):
    command = input().strip().split()
    if (command[0] == 'push_front'):
        numdeque.appendleft(command[1])
    if(command[0] == 'push_back'):
        numdeque.append(command[1])
    if(command[0] == 'pop_front'):
        if(numdeque):
            temp = numdeque.popleft()
            print("%d" %(int(temp)))
            continue
        print("-1")
    if(command[0] == 'pop_back'):
        if(numdeque):
            temp = numdeque.pop()
            print("%d" %(int(temp)))
            continue
        print("-1")
    if(command[0] == 'size'):
        print(len(numdeque))
    if(command[0] == 'empty'):
        if(numdeque):
            print("0")
            continue
        print("1")
    if(command[0]=="front"):
        if(numdeque):
            temp = numdeque.popleft()
            print("%d" %(int(temp)))
            numdeque.appendleft(temp)
            continue
        print("-1")
    if(command[0]=='back'):
        if(numdeque):
            temp = numdeque.pop()
            print("%d" %(int(temp)))
            numdeque.append(temp)
            continue
        print("-1")