import sys

input = sys.stdin.readline


def dp(n):
    if n == 1:
        return 0
    if n == 2 or n == 3:
        return 1
    if n not in memo:
        if n % 6 == 0:
            memo[n] = min(dp(n // 3), dp(n // 2)) + 1
        elif n % 6 == 3:
            memo[n] = min(dp(n // 3), dp(n - 1)) + 1
        elif n % 6 == 4:
            memo[n] = min(dp(n // 2), dp(n - 1)) + 1
        elif n % 6 == 1:
            memo[n] = dp(n - 1) + 1
        elif n % 6 == 2:
            memo[n] = min(dp(n // 2), dp(n - 1)) + 1
        else:
            memo[n] = dp(n - 1) + 1
    return memo[n]


memo = {}
memo[1] = 0
memo[2] = 1
memo[3] = 1
answer = dp(int(input().strip()))
print("%d" % answer)
