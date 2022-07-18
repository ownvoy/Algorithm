import sys
from collections import deque

input = sys.stdin.readline

vertex, edge, start = list(map(int, input().strip().split()))

matrix = [[0] * (vertex + 1) for _ in range(vertex + 1)]

visited = [0 for i in range(vertex + 1)]

for _ in range(edge):
    v1, v2 = map(int, input().strip().split())
    matrix[v1][v2] = 1
    matrix[v2][v1] = 1


def bfs(start):
    visited[start] = 0
    queue = deque([])
    queue.append(start)

    while queue:
        vv = queue.popleft()
        print(vv, end=" ")
        for pair in range(1, vertex + 1):
            if matrix[vv][pair] == 1 and visited[pair] == 1:
                queue.append(pair)
                visited[pair] = 0


def dfs(start):
    visited[start] = 1
    print(start, end=" ")
    for pair in range(1, vertex + 1):
        if matrix[start][pair] == 1 and visited[pair] == 0:
            dfs(pair)


dfs(start)
print()
bfs(start)
