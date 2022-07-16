import sys

input = sys.stdin.readline

A, B, V = list(map(int, input().strip().split()))
distance = A - B

approx = (V - A) // distance

if approx * distance + A >= V:
    approx += 1
else:
    approx += 2

print(approx)
