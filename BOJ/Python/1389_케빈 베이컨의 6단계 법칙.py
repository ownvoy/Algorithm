import sys
from collections import deque

input = sys.stdin.readline

vertex, edge = map(int, input().strip().split())
matrix = [[0] * (vertex + 1) for _ in range(vertex + 1)]

for _ in range(edge):
    v1, v2 = map(int, input().strip().split())
    matrix[v1][v2] = 1
    matrix[v2][v1] = 1


def bfs(start):
    temp = matrix
    visited = [0] * (vertex + 1)
    num = [0] * (vertex + 1)
    queue = deque([])
    visited[start] = 1
    queue.append(start)
    while queue:
        vv = queue.popleft()
        for pair in range(1, vertex + 1):
            if visited[pair] == 0 and temp[vv][pair] == 1:
                num[pair] = num[vv] + 1
                visited[pair] = 1
                queue.append(pair)
    return sum(num)


result = []

for i in range(1, vertex + 1):
    result.append(bfs(i))

print(result.index(min(result)) + 1)
