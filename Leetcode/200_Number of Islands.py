from collections import deque


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        dM = [-1, 0, 0, 1]
        dN = [0, -1, 1, 0]
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    queue.append([i, j])
                    while queue:
                        currM, currN = queue.popleft()
                        for h in range(4):
                            nextM = currM + dM[h]
                            nextN = currN + dN[h]
                            if 0 <= nextM < m and 0 <= nextN < n:
                                if grid[nextM][nextN] == "1":
                                    queue.append([nextM, nextN])
                                    grid[nextM][nextN] = "0"
                    count += 1
        return count


solution = Solution()
answer1 = solution.numIslands(
    [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
)

solution = Solution()
answer2 = solution.numIslands(
    grid=[
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
)
