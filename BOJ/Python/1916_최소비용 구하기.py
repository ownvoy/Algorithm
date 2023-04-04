from heapq import heappop, heappush


v = int(input())
e = int(input())
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

start, destination = map(int, input().split())
distance = [float("inf") for _ in range(v + 1)]

heap = [[0, start]]
distance[start] = 0
while heap:
    ww, vv = heappop(heap)
    if distance[vv] < ww:
        continue
    for vvv, www in graph[vv]:
        cost = www + ww
        if cost < distance[vvv]:
            distance[vvv] = cost
            heappush(heap, [cost, vvv])

print(distance[destination])
