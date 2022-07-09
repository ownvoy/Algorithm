import sys
input = sys.stdin.readline
testcase = int(input().strip())
b = [input().strip().split() for _ in range(testcase)]
for word in b:
    for i in range(len(word)):
        word[i] = "".join(list(word[i])[::-1])
    print(" ".join(word))
    
