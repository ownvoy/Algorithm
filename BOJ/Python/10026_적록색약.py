import copy
import sys
from collections import deque

input = sys.stdin.readline


n = int(input().strip())
matrix = [list(input().strip()) for _ in range(n)]
matrix2 = copy.deepcopy(matrix)
result = []

for i in range(n):
    for j in range(n):
        if matrix2[i][j] == "G":
            matrix2[i][j] = "R"


dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]


def bfs(mtr):
    count = 0
    for i in range(n):
        for j in range(n):
            if mtr[i][j] != -1:
                queue = deque()
                queue.append([i, j])
                color = mtr[i][j]
                while queue:
                    currX, currY = queue.popleft()
                    for k in range(4):
                        nextX = currX + dx[k]
                        nextY = currY + dy[k]
                        if 0 <= nextX < n and 0 <= nextY < n:
                            if mtr[nextX][nextY] == color:
                                mtr[nextX][nextY] = -1
                                queue.append([nextX, nextY])
                count += 1
    global result
    result.append(count)


bfs(matrix)
bfs(matrix2)

print(*result)
