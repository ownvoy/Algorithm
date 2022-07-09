import sys
input = sys.stdin.readline

N = int(input())

word_list = [input().strip() for _ in range(N)]
temp = set(word_list)
word_list = list(temp)
word_list.sort()

word_list.sort(key = len)

for word in word_list:
    print(word)