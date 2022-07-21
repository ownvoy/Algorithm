import sys

input = sys.stdin.readline

N = int(input().strip())
num_list = list(map(int, input().strip().split()))

idx = 1
memo = {}
for number in num_list:
    memo[idx] = number
    idx += 1

memo_sort = sorted(memo.items(), key=lambda x: x[1])
accum = 0
total = 0
for minute in memo_sort:
    accum += minute[1]
    total += accum
print(total)
