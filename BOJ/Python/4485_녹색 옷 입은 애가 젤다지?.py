from heapq import heappop, heappush


def dijkstra(graph, a):
    distance = [[float("inf") for _ in range(a)] for _ in range(a)]
    heap = [[graph[0][0], 0, 0]]
    dc = [-1, 0, 0, 1]
    dr = [0, 1, -1, 0]
    distance[0][0] = graph[0][0]
    while heap:
        weight, col, row = heappop(heap)
        if weight > distance[col][row]:
            continue
        for i in range(4):
            nc = col + dc[i]
            nr = row + dr[i]
            if 0 <= nc < a and 0 <= nr < a:
                cost = weight + graph[nc][nr]
                if cost < distance[nc][nr]:
                    distance[nc][nr] = cost
                    heappush(heap, [cost, nc, nr])
    return distance[a - 1][a - 1]


a = 10000
problem = 1
while True:
    a = int(input())
    if a == 0:
        break
    graph = []
    for _ in range(a):
        row = map(int, input().split())
        graph.append(list(row))
    result = dijkstra(graph, a)
    print(f"Problem {problem}:", result)
    problem += 1
