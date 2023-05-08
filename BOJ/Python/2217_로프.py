
n = int(input())

weight = []
result = []

for i in range(n):
    weight.append(int(input()))

weight.sort(reverse=True)

while weight:
    a = weight.pop()
    result.append(a*(len(weight)+1))

print(max(result))
