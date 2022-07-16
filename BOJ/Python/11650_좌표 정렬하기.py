import sys
from operator import itemgetter

input = sys.stdin.readline

number = int(input().strip())

numlist = [list(map(int, input().strip().split())) for _ in range(number)]
numlist = sorted(numlist, key=itemgetter(0, 1))

for i in range(number):
    print(numlist[i][0], end=" ")
    print(numlist[i][1])
