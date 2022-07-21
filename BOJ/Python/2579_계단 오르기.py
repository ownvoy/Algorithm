import sys

sys.setrecursionlimit(10**5)
input = sys.stdin.readline

number = int(input().strip())
num_list = [int(input().strip()) for _ in range(number)]
memo = {}


def dp(n):
    if n == 0:
        memo[0] = num_list[0]
        return memo[0]
    if n == 1:
        memo[1] = num_list[1] + num_list[0]
        return memo[1]
    if n == 2:
        memo[2] = max(num_list[0] + num_list[2], num_list[1] + num_list[2])
        return memo[2]
    if n not in memo:
        memo[n] = max(
            dp(n - 3) + num_list[n - 1] + num_list[n], num_list[n] + dp(n - 2)
        )
    return memo[n]


print(dp(number - 1))
