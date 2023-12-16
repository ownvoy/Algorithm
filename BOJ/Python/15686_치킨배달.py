from itertools import combinations

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dc = [-1, 0, 0, 1]
dr = [0, 1, -1, 0]
houses = []
chickens = []

for row in range(n):
    for col in range(n):
        if graph[row][col] == 1:
            houses.append([row, col])
        if graph[row][col] == 2:
            chickens.append([row, col])

total = float("inf")

for c in list(combinations(chickens, m)):
    dist = 0
    for i in houses:
        i_dist = float("inf")
        for rr, cc in c:
            i_dist = min(abs(rr - i[0]) + abs(cc - i[1]), i_dist)
        dist += i_dist
    total = min(dist, total)

print(total)
