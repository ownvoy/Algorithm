import sys

input = sys.stdin.readline
N, M = map(int, input().strip().split())
numlist = list(map(int, input().strip().split()))
prefix_sum = [0]
sumsum = 0
for i in numlist:
    sumsum += i
    prefix_sum.append(sumsum)

for _ in range(M):
    start, end = map(int, input().strip().split())
    print(prefix_sum[end] - prefix_sum[start - 1])
