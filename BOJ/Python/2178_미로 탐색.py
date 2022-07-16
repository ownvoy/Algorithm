import sys
from collections import deque

input = sys.stdin.readline

m, n = list(map(int, input().strip().split()))
matrix = [list(map(int, list(input().strip()))) for _ in range(m)]


def solution(matrix, m, n):
    queue = deque()
    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]

    check_map = [[False] * n for _ in range(m)]
    dist_map = [[0] * n for _ in range(m)]
    dist_map[0][0] = 1
    check_map[0][0] = True
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nextX = x + dx[i]
            nextY = y + dy[i]
            if 0 <= nextX < n and 0 <= nextY < m:
                if matrix[nextY][nextX] == 1 and check_map[nextY][nextX] is False:
                    dist_map[nextY][nextX] = dist_map[y][x] + 1
                    check_map[nextY][nextX] = True
                    queue.append((nextX, nextY))
    print(dist_map[m - 1][n - 1])


solution(matrix, m, n)
