import sys

num_dict = {}

input = sys.stdin.readline
N = int(input().strip())
num_list = input().strip().split()
for num in num_list:
    num_dict[num] = 1

M = int(input().strip())
test_list = input().strip().split()

for number in test_list:
    if number not in num_dict:
        num_dict[number] = 0
    print(num_dict[number])
