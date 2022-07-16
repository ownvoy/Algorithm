import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def dp(n):
    if n == 1 or n == 2 or n == 4:
        return -5000
    if n == 3 or n == 5:
        return 1
    if n not in memo:
        if dp(n - 3) > 0 and dp(n - 5) > 0:
            memo[n] = min(dp(n - 3), dp(n - 5)) + 1
        elif dp(n - 3) < 0 and dp(n - 5) > 0:
            memo[n] = dp(n - 5) + 1
        elif dp(n - 5) < 0 and dp(n - 3) > 0:
            memo[n] = dp(n - 3) + 1
        elif dp(n - 3) < 0 and dp(n - 5) < 0:
            memo[n] = dp(n - 5) + 1
    return memo[n]


memo = {}
memo[1] = -5000
memo[2] = -5000
memo[4] = -5000
memo[3] = 1
memo[5] = 1

n = int(input().strip())

answer = dp(n)
if answer > 0:
    print(answer)
else:
    print("-1")
