import math

t = int(input())
for i in range(t):
    x, y = list(map(int, input().split()))
    length = y - x

    n = math.floor(((-1) + (1 + 4 * length) ** (1 / 2)) / 2)
    remainder = length - n * (n + 1)
    operations = 2 * n

    if 0 < remainder <= n + 1:
        operations += 1
    elif remainder > n + 1:
        operations += 2

    print(operations)
