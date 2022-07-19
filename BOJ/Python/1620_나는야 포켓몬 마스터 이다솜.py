import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())

memo = {}
for i in range(1, N + 1):
    memo[i] = input().strip()

memo.update(dict(zip(memo.values(), memo.keys())))

for _ in range(M):
    result = input().strip()
    if result not in memo:
        print(memo[int(result)])
    else:
        print(memo[result])
