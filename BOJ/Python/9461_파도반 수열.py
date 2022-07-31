import sys

input = sys.stdin.readline

N = int(input().strip())
memo = {}
memo[1] = 1
memo[2] = 1
memo[3] = 1
memo[4] = 2
memo[5] = 2


def dp(n):
    if n in memo:
        return memo[n]
    else:
        memo[n] = dp(n - 1) + dp(n - 5)
        return memo[n]


for _ in range(N):
    result = dp(int(input().strip()))
    print("%d" % result)
