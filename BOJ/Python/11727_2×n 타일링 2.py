import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input().strip())

memo = {}
memo[1] = 1
memo[2] = 3


def dp(number):
    if number == 1:
        return memo[1]
    elif number == 2:
        return memo[2]
    else:
        if number not in memo:
            memo[number] = dp(number - 1) + dp(number - 2) * 2
        return memo[number]


result = dp(n) % 10007

print("%d" % result)
