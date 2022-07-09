import sys
input = sys.stdin.readline

group_count = int(input())
a = [input().strip() for _ in range(group_count)]

for word in a:
    for i in range(len(word)-1):
        if(word[i]== word[i+1]):
            pass
        elif(word[i] in word[i+2:]):
            group_count -= 1
            break
print(group_count)