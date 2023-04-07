n = int(input())
result = 0

for i in range(1, n + 1):
    if len(str(i)) <= 2:
        result += 1
    elif len(str(i)) == 3:
        num = str(i)
        if int(num[1]) - int(num[0]) == int(num[2]) - int(num[1]):
            result += 1

print(result)
