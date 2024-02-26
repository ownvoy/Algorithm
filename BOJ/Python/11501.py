N = int(input())


def max_benefit():
    days = int(input())
    prices = list(map(int, input().split()))
    maxs = [0 for _ in range(len(prices))]
    temp = 0
    for i in range(len(prices) - 1, -1, -1):
        maxs[i] = max(prices[i], temp)
        temp = maxs[i]
    result = 0
    for m, p in zip(maxs, prices):
        result += max(m - p, 0)
    return result


for _ in range(N):
    result = max_benefit()
    print(result)
