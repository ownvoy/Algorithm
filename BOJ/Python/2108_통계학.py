import sys
from operator import itemgetter

input = sys.stdin.readline

number = int(input().strip())
numlist = [int(input().strip()) for _ in range(number)]
sorted_list = sorted(numlist)

totalsum = 0
memo = {}
for num in numlist:
    totalsum += num
    if num not in memo:
        memo[num] = 1
    else:
        memo[num] += 1

print("%d" % round(totalsum / number))  # 산술평균
print(sorted_list[number // 2])  # 중앙값


sorted_memo = list(map(list, sorted(memo.items(), key=itemgetter(1, 0))))
max_freq = sorted_memo[len(sorted_memo) - 1][1]
count = 0
for memo in sorted_memo:
    if memo[1] == max_freq:
        count += 1
    if count == 2:
        print(memo[0])
        break
if count == 1:
    print(sorted_memo[len(sorted_memo) - 1][0])

print("%d" % (sorted_list[number - 1] - sorted_list[0]))  # 범위
