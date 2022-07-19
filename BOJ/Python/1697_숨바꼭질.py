import sys
from collections import deque

input = sys.stdin.readline

subin, sister = map(int, input().strip().split())
num = {}


def bfs():
    queue = deque([])
    queue.append(subin)
    num[subin] = 0
    while queue:
        vv = queue.popleft()
        if vv == sister:
            break
        for nextX in [vv - 1, vv + 1, vv * 2]:
            if 0 <= nextX <= 10**5 and nextX not in num:
                queue.append(nextX)
                num[nextX] = num[vv] + 1
    return num[vv]


result = bfs()
print(result)
