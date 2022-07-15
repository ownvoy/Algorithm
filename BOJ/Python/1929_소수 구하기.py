import math
import sys

input = sys.stdin.readline

M, N = input().strip().split()
init_num = int(M)
last_num = int(N)
prime_dict = {}
for i in range(2, last_num + 1):
    Isprime = 0
    for prime in prime_dict:
        if i % prime == 0:
            Isprime = 1
            break
        if prime > math.sqrt(i):
            break
    if Isprime == 0:
        prime_dict[i] = 0
        if i >= init_num:
            print(i)
