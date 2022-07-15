import sys

input = sys.stdin.readline

number = 2
prime = {}
prime[1] = 0

while number <= 1000:
    divide_num = 2
    while divide_num < number:
        if number % divide_num == 0:
            prime[number] = 0
            break
        divide_num += 1
    if number not in prime:
        prime[number] = 1
    number += 1

N = input().strip()
count = 0
num_list = list(map(int, input().strip().split()))
for num in num_list:
    count += prime[num]

print(count)
