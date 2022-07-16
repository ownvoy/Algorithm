import sys
from operator import itemgetter

input = sys.stdin.readline

number = int(input().strip())

numlist = [input().strip().split() for _ in range(number)]

for i in range(number):
    numlist[i][0] = int(numlist[i][0])

numlist = sorted(numlist, key=itemgetter(0))
for info in numlist:
    print(*info)
