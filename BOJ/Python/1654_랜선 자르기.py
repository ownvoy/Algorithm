
import sys

input = sys.stdin.readline

K, N = map(int, input().split())
cable = [int(input()) for _ in range(K)]

cable_max = 0

start = 1
end = max(cable)

while start <= end:
    mid = (start + end)//2
    count = 0
    for i in cable:
        count += i // mid
    if count >= N:
        start = mid +1
        cable_max = mid
    else:
        end = mid - 1
        
print(cable_max)