import sys

input = sys.stdin.readline

memo = {}
memo[1] = 1
memo[2] = 2
memo[3] = 4


def ffibo(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    if n not in memo:
        memo[n] = ffibo(n - 1) + ffibo(n - 2) + ffibo(n - 3)
        return memo[n]
    return memo[n]


testcase = int(input().strip())

for _ in range(testcase):
    print(ffibo(int(input().strip())))
