import sys
from operator import itemgetter

input = sys.stdin.readline

number = int(input().strip())
info = []
for _ in range(number):
    info.append(list(map(int, input().strip().split())))

info = sorted(info, key=lambda a: a[0])
info = sorted(info, key=lambda a: a[1])

last = 0
count = 0
for start, end in info:
    if start >= last:
        count += 1
        last = end
print(count)
