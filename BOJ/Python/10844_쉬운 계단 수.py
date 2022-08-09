import sys

input = sys.stdin.readline

memo = {}

for k in range(10):
    memo[k] = 1
memo[0] = 0


def dp(n):
    total = 0
    for i in range(n - 1):
        temp = {}

        temp[0] = memo[1]
        for p in range(1, 9):
            temp[p] = memo[p - 1] + memo[p + 1]
        temp[9] = memo[8]

        for j in range(10):
            memo[j] = temp[j]
    for h in range(10):
        total += memo[h]
    print(total % 1000000000)


number = int(input().strip())
dp(number)
