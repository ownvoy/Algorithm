
import sys 
input = sys.stdin.readline
word = sorted(input().strip())
count = [0]*26

for character in word:
    asc = ord(character)-97
    count[asc]+=1
print(*count)
    