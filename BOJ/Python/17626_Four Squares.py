import sys

input = sys.stdin.readline
n = int(input())
numlist = [0] * (n + 1)
numlist[1] = 1
for i in range(2, n + 1):
    j = 1
    minvalue = 4
    while (j**2) <= i:
        a = numlist[i - (j**2)] + 1
        minvalue = min(minvalue, a)
        j += 1
    numlist[i] = minvalue
print(numlist[n])
