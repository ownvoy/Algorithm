import sys
from collections import deque

input = sys.stdin.readline

number = int(input().strip())

matrix = [[] for _ in range(number + 1)]

for _ in range(number - 1):
    a, b = map(int, input().strip().split())
    matrix[a].append(b)
    matrix[b].append(a)

memo = {}


def bfs():
    queue = deque()
    queue.append(1)
    while queue:
        curr = queue.popleft()
        for i in matrix[curr]:
            queue.append(i)
            if i not in memo:
                memo[i] = curr
        matrix[curr].clear()


bfs()
for i in range(2, number + 1):
    print(memo[i])
