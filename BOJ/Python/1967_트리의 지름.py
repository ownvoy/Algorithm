import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

number = int(input().strip())
graph = [[] for _ in range(number + 1)]

for _ in range(number - 1):
    node1, node2, weight = map(int, input().strip().split())
    graph[node1].append([node2, weight])
    graph[node2].append([node1, weight])

distance = [-1] * (number + 1)
distance[1] = 0


def dfs(number, weight):
    for i in graph[number]:
        node, b = i
        if distance[node] == -1:
            distance[node] = weight + b
            dfs(node, weight + b)


dfs(1, 0)

start = distance.index(max(distance))
distance = [-1] * (number + 1)
distance[start] = 0
dfs(start, 0)

print(max(distance))
