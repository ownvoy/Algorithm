import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())

memo = {}
for _ in range(N):
    memo[input().strip()] = 1

namelist = []
for _ in range(M):
    name = input().strip()
    if name in memo:
        namelist.append(name)

print(len(namelist))
print("\n".join(sorted(namelist)))
