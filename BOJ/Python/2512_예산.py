n = int(input())
wants = list(map(int, input().split()))
total = int(input())
max_money = 0
wants.sort()

prev = 0
minn = wants.pop(0)
flag = 0

while wants:
    request = minn - prev
    num = len(wants) + 1
    if total - num * request >= 0:
        total -= num * request
        max_money += request
    else:
        max_money += total // num
        flag = 1
        break
    prev = minn
    minn = wants.pop(0)

if flag == 0:
    max_money += minn - prev

print(max_money)
