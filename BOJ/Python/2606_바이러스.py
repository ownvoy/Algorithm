import sys
from collections import deque

input = sys.stdin.readline

vertex = int(input().strip())
edge = int(input().strip())

matrix = [[0] * (vertex + 1) for _ in range(vertex + 1)]

for _ in range(edge):
    vv1, vv2 = map(int, input().strip().split())
    matrix[vv1][vv2] = 1
    matrix[vv2][vv1] = 1

check_list = [0] * (vertex + 1)


def bfs():
    count = 0
    queue = deque([])
    queue.append(1)
    check_list[1] = 1
    while queue:
        vv = queue.popleft()
        for i in range(vertex + 1):
            if matrix[vv][i] == 1 and check_list[i] == 0:
                count += 1
                check_list[i] = 1
                matrix[vv][i] = 0
                queue.append(i)
    return count


print(bfs())
