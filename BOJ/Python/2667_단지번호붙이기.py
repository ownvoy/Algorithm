# dfs (섬 문제, 1012_유기농 배추와 유사)
import sys

input = sys.stdin.readline

N = int(input().strip())
matrix = [list(map(int, list(input().strip()))) for _ in range(N)]
count = 0
result = []


def dfs():
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                count = 1
                stack = []
                stack.append([i, j])
                while stack:
                    row, col = stack.pop()
                    matrix[row][col] = 0
                    nexts = [[-1, 0], [1, 0], [0, 1], [0, -1]]
                    for h in range(4):
                        nextR, nextC = nexts[h]
                        if 0 <= row + nextR < N and 0 <= col + nextC < N:
                            if matrix[row + nextR][col + nextC] == 1:
                                matrix[row + nextR][col + nextC] = 0
                                count += 1
                                stack.append([row + nextR, col + nextC])
                result.append(count)


dfs()
print(len(result))
print("\n".join(map(str, sorted(result))))
