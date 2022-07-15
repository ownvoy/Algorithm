import sys

input = sys.stdin.readline

N = int(input().strip())
num_dict = {}
num_list = input().strip().split()
for number in num_list:
    if number not in num_dict:
        num_dict[number] = 1
        continue
    num_dict[number] += 1
M = int(input().strip())
testcase = input().strip().split()

for number in testcase:
    if number not in num_dict:
        print("0", end=" ")
        continue
    print(num_dict[number], end=" ")
