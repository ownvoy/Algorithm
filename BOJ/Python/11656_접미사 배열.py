import sys
input = sys.stdin.readline

dic = list(input().strip())
dic_len = len(dic)
suffix = []
for i in range(dic_len):
    suffix.append(dic[i:])
temp = []

for word in suffix:
    temp.append("".join(word))

for word in sorted(temp):
    print(word)
