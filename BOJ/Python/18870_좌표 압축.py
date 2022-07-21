import sys

input = sys.stdin.readline
input().strip()
num_list = list(map(int, input().strip().split()))
num_dict = {}
for number in num_list:
    if number not in num_dict:
        num_dict[number] = 1

num_sort = sorted(num_dict.keys())
i = 0
for number in num_sort:
    num_dict[number] = i
    i += 1

for number in num_list:
    print(num_dict[number], end=" ")
