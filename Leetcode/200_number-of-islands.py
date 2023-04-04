# @before-stub-for-debug-begin
from python3problem200 import *
from typing import *

# @before-stub-for-debug-end

#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def __init__(self):
        self.result = 0
        self.dc = [0, 1, -1, 0]
        self.dr = [1, 0, 0, -1]

    def numIslands(self, grid: List[List[str]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.result += 1
                    grid[i][j] = "0"
                    self.dfs(grid, i, j)
        return self.result

    def dfs(self, grid, row, col):
        for j in range(4):
            if 0 <= row + self.dr[j] < len(grid) and 0 <= col + self.dc[j] < len(grid[0]):
                if grid[row + self.dr[j]][col + self.dc[j]] == "1":
                    grid[row + self.dr[j]][col + self.dc[j]] = "0"
                    self.dfs(grid, row + self.dr[j], col + self.dc[j])


# @lc code=end
