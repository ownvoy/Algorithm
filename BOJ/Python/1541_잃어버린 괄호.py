import sys

input = sys.stdin.readline

polynomial = input().strip().split("-")

count = 0
result = 0

for plus in polynomial:
    plus = list(map(int, "".join(plus).split("+")))
    each_sum = 0
    for i in plus:
        each_sum += i
    count += 1
    if count == 1:
        result += each_sum
    else:
        result -= each_sum

print(result)
