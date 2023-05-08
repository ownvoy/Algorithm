from collections import deque

n, k = list(map(int, input().split()))
yosepus = deque([i for i in range(1, n + 1)])
result = []

start = 1
while yosepus:
    if start != k:
        element = yosepus.popleft()
        yosepus.append(element)
        start += 1
    else:
        element = yosepus.popleft()
        result.append(element)
        start = 1


print("<", end="")
print(*result, sep=", ", end="")
print(">")
