n, c = list(map(int, input().split()))
houses = []
for i in range(n):
    houses.append(int(input()))

houses.sort()
minn = 1
maxx = houses[-1] - houses[0]
result = 0

while minn <= maxx:
    mid = (minn + maxx) // 2
    count = 1
    current = houses[0]

    for i in range(1, len(houses)):
        if houses[i] >= current + mid:
            count += 1
            current = houses[i]
    if count >= c:
        minn = mid + 1
        result = mid
    else:
        maxx = mid - 1
print(result)
