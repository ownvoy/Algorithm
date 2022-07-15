import sys

input = sys.stdin.readline
N = int(input().strip()) - 1
num_666list = []
i = "666"
while len(num_666list) != 10000:
    if "666" in i:
        num_666list.append(i)

    temp = int(i)
    temp += 1
    i = str(temp)


print(num_666list[N])
