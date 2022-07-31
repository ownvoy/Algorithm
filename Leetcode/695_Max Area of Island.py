from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        dr = [-1, 0, 0, 1]
        dc = [0, 1, -1, 0]
        memo = {}
        idx = 0
        count = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append([i, j])
                    grid[i][j] = 0
                    while queue:
                        row, col = queue.popleft()
                        for h in range(4):
                            nextR = row + dr[h]
                            nextC = col + dc[h]
                            if 0 <= nextR < m and 0 <= nextC < n:
                                if grid[nextR][nextC] == 1:
                                    grid[nextR][nextC] = 0
                                    queue.append([nextR, nextC])
                                    count += 1
                    memo[idx] = count
                    count = 1
                    idx += 1
        result = memo.values()
        if result:
            # print(max(result))
            return max(result)
        else:
            # print("0")
            return 0


# solution = Solution()
# solution.maxAreaOfIsland(
#     grid=[
#         [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
#         [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
#         [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
#     ]
# )

solution2 = Solution()
solution2.maxAreaOfIsland(grid=[[1, 0]])
