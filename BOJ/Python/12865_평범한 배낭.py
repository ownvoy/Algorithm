n, k = map(int, input().split())

weights = []
result = [0 for i in range(k + 1)]


for i in range(n):
    w, v = map(int, input().split())
    weights.append([w, v])


for item in weights:
    w, v = item
    for i in range(k, w - 1, -1):
        result[i] = max(result[i], result[i - w] + v)

print(result[-1])
