import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(x, y):
    visited[x][y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        nextX, nextY = x + dx, y + dy
        if nextX < 0 or nextX >= row or nextY < 0 or nextY >= column:
            continue
        if array[nextX][nextY] and not visited[nextX][nextY]:
            dfs(nextX, nextY)


for _ in range(int(input())):
    column, row, k = map(int, input().strip().split())

    array = [[0] * column for _ in range(row)]
    visited = [[False] * column for _ in range(row)]

    for _ in range(k):
        y, x = map(int, input().split())
        array[x][y] = 1

    result = 0
    for i in range(row):
        for j in range(column):
            if array[i][j] and not visited[i][j]:
                dfs(i, j)
                result += 1

    print(result)
