import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
vertex, edge = map(int, input().strip().split())

matrix = [[0] * (vertex + 1) for _ in range(vertex + 1)]
check_list = [0] * (vertex + 1)
check_list[0] = 1
for _ in range(edge):
    row, col = map(int, input().strip().split())
    matrix[row][col] = 1
    matrix[col][row] = 1

start = 1


def ddfs(start):
    check_list[start] = 1
    for index, pair in enumerate(matrix[start]):
        if pair == 1 and check_list[index] == 0:
            ddfs(index)


i = 0
count = 0

while 0 in check_list:
    ddfs(i)
    for i, v in enumerate(check_list):
        if v == 0:
            count += 1
            ddfs(i)

print(count)
