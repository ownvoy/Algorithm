import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().strip().split())
ladder = {}
snake = {}
for _ in range(N):
    down, up = map(int, input().strip().split())
    ladder[down] = up

for _ in range(M):
    up, down = map(int, input().strip().split())
    snake[up] = down
count = {}


def move(i):
    if i in ladder:
        i = ladder[i]
    elif i in snake:
        i = snake[i]
    return i


def bfs():
    queue = deque()
    for i in range(2, 8):
        i = move(i)
        count[i] = 1
        queue.append(i)
    while queue:
        curr = queue.popleft()
        for j in range(1, 7):
            nextP = curr + j
            nextP = move(nextP)
            if nextP not in count:
                count[nextP] = count[curr] + 1
                queue.append(nextP)
        if 100 in count:
            print(count[100])
            return


bfs()
