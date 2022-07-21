import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())
memo = {}

for _ in range(N):
    site, password = input().strip().split()
    memo[site] = password

for _ in range(M):
    print(memo[input().strip()])
