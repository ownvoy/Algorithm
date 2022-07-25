import sys
from collections import deque

input = sys.stdin.readline

col, row = map(int, input().strip().split())

matrix = []
for _ in range(row):
    matrix.append(list(map(int, input().strip().split())))

# count = [[0] * (col)] * row
count = [[0 for _ in range(col)] for _ in range(row)]


def bfs():
    queue = deque()
    nextP = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 1:
                queue.append([i, j])
                matrix[i][j] = -2
    while queue:
        cur_row, cur_col = queue.popleft()
        for h in range(4):
            nextR = cur_row + nextP[h][0]
            nextC = cur_col + nextP[h][1]
            if 0 <= nextR < row and 0 <= nextC < col:
                if matrix[nextR][nextC] == 0:
                    matrix[nextR][nextC] = -2
                    count[nextR][nextC] = count[cur_row][cur_col] + 1
                    queue.append([nextR, nextC])


def check():
    each_max = []
    for i in range(row):
        each_max.append(max(count[i]))
        for j in range(col):
            if matrix[i][j] == 0:
                print(-1)
                return
    print("%d" % max(each_max))


bfs()
check()
