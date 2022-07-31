import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().strip().split())

storage = []
for _ in range(H):
    box = []
    for _ in range(N):
        row = list(map(int, input().strip().split()))
        box.append(row)
    storage.append(box)

check = [[[-2 for _ in range(M)] for _ in range(N)] for _ in range(H)]

queue = deque()
for i in range(H):  # 높이
    for j in range(N):  # row
        for k in range(M):  # col
            if storage[i][j][k] == 1:
                queue.append([i, j, k])
                storage[i][j][k] = 2
                check[i][j][k] = 0

dx = [-1, 0, 0, 1, 0, 0]
dy = [0, -1, 1, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

while queue:
    currH, currN, currM = queue.popleft()
    for h in range(6):

        nextH = currH + dx[h]  # H
        nextN = currN + dy[h]  # N
        nextM = currM + dz[h]  # M
        if 0 <= nextH < H and 0 <= nextN < N and 0 <= nextM < M:
            if storage[nextH][nextN][nextM] == 0:
                storage[nextH][nextN][nextM] = 2
                check[nextH][nextN][nextM] = check[currH][currN][currM] + 1
                queue.append([nextH, nextN, nextM])

i = 0
j = 0

result = 0
max_days = []
for i in range(H):  # 높이
    for j in range(N):  # row
        max_days.append(max(check[i][j]))
        if 0 in storage[i][j]:
            result = 1
            break

if result == 1:
    print("-1")
else:
    print(max(max_days))
