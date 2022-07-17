import sys

input = sys.stdin.readline
memo0 = {}
memo1 = {}

memo0[0] = 1
memo0[1] = 0
memo1[0] = 0
memo1[1] = 1


def fibo(n):
    if n == 0:
        return 1, 0
    elif n == 1:
        return 0, 1
    else:
        if n not in memo0:
            temp0, temp1 = fibo(n - 1)
            temp2, temp3 = fibo(n - 2)
            memo0[n] = temp0 + temp2
            memo1[n] = temp1 + temp3
        return memo0[n], memo1[n]


for _ in range(int(input().strip())):
    number = int(input().strip())
    result0, result1 = fibo(number)
    print("%d" % result0, end=" ")
    print("%d" % result1)
