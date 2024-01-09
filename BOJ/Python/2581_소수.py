from math import sqrt


m = int(input())
n = int(input())
total = 0
minn = 0
prime = 1

for num in range(m, n + 1):
    prime = 1
    root = int(sqrt(num))
    for i in range(2, num):
        if num % i == 0:
            prime = 0
            break

    if prime == 1 and num != 1:
        if total == 0:
            minn = num
        total += num

if total != 0:
    print(total)
    print(minn)
else:
    print(-1)
