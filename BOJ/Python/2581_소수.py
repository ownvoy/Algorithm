from math import sqrt


m = int(input())
n = int(input())

total_sum = 0
min_prime = 0

for num in range(m, n + 1):
    if num > 1:  # 1은 소수가 아님
        is_prime = True
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            if total_sum == 0:
                min_prime = num
            total_sum += num

if total_sum != 0:
    print(total_sum)
    print(min_prime)
else:
    print(-1)
