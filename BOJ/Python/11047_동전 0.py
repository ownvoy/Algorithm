import sys

intput = sys.stdin.readline

number, total = map(int, input().strip().split())

unit_list = []
for _ in range(number):
    unit = int(input().strip())
    unit_list.append(unit)

unit_list = sorted(unit_list, reverse=True)
count = 0

for unit in unit_list:
    quoitent = total // unit
    count += quoitent
    total -= quoitent * unit
    if total == 0:
        break

print(count)
