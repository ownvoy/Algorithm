import heapq

vertex, edge = map(int, input().split())
root = int(input())
distance = [float("inf")] * (vertex + 1)
graph = [[] for _ in range(vertex + 1)]


for _ in range(edge):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])


def dijkstra(root):
    q = []
    heapq.heappush(q, (0, root))
    distance[root] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for vv, ww in graph[now]:
            cost = distance[now] + ww
            if cost < distance[vv]:
                distance[vv] = cost
                heapq.heappush(q, (cost, vv))


dijkstra(root)

for i in range(1, vertex + 1):
    if distance[i] == float("inf"):
        print("INF")
    else:
        print(distance[i])
