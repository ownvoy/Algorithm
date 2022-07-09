
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
circle = [ i+1 for i in range(n)]

index = 0 
print("<", end="")
while(len(circle)):
    index += (k-1)
    if(index >=len(circle)):
        index %= len(circle)
    a= circle.pop(index)
    print(a, end = '')
    while(len(circle)):
        print(", ", end = '')
        break
print(">")