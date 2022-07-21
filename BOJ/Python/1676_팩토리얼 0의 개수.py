import sys

input = sys.stdin.readline

N = int(input().strip())

count = 0
for i in range(1, N + 1):
    if i % 5 == 0:
        temp = i
        while temp % 5 == 0:
            temp = temp // 5
            count += 1

print(count)
