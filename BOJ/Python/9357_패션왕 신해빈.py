import sys

input = sys.stdin.readline

for _ in range(int(input().strip())):
    memo = {}
    for _ in range(int(input().strip())):
        product, classification = input().strip().split()
        if classification not in memo:
            memo[classification] = 1
        else:
            memo[classification] += 1
    result = 1
    if memo:
        for classification in memo:
            result *= memo[classification] + 1
        print("%d" % (result - 1))
    else:
        print("0")
