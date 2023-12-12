n = int(input())


def dp(n):
    if n == 1:
        return 1
    else:
        return 2 * dp(n - 1) + 1


result1 = dp(n)
print(result1)

order = {}


def dp2(n, start, mid, end):
    if n == 1:
        return [start, end]
    else:
        order[n] = (
            dp2(n - 1, start, end, mid) + [start, end] + dp2(n - 1, mid, start, end)
        )
    return order[n]


l = 0
result2 = dp2(n, 1, 2, 3)
for r in result2:
    if l == 0:
        print(r, end=" ")
        l = 1
        continue
    if l == 1:
        print(str(r))
        l = 0
        continue


"""
def dp(n, start, mid, end):
    if n == 1:
        print(start, end)
    else:
        dp(n-1, start, end, mid)
        print(start, end)
        dp(n-1, mid, start, end)

n = int(input())
print(2**n-1)
dp(n, 1, 2, 3)

"""
