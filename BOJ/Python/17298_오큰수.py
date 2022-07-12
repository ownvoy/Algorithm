import sys
from collections import deque


input = sys.stdin.readline
number = int(input().strip())
numlist = list(map(int, input().strip().split()))
stack = deque()
nge = [-1]*number

for i in range(number):
    while stack and (stack[-1][0]< numlist[i]):
        tmp, idx = stack.pop()
        nge[idx] =numlist[i]
    stack.append([numlist[i],i])

print(*nge)
