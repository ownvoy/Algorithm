import math
import sys

input = sys.stdin.readline

number = int(input().strip())


def count(n):
    one_count = n
    two_count = 0
    result = 0
    while one_count >= 0:
        result += (
            math.factorial(one_count + two_count)
            // math.factorial(one_count)
            // math.factorial(two_count)
        )
        one_count -= 2
        two_count += 1
    print(result % 10007)


count(number)
