# @before-stub-for-debug-begin
from python3problem130 import *
from typing import *

# @before-stub-for-debug-end

#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = []
        stack = []
        row = len(board)
        col = len(board[0])
        dr = [1, 0, 0, -1]
        dc = [0, -1, 1, 0]
        for i in range(row):
            for j in range(col):
                if i == 0 or i == row - 1 or j == 0 or j == col - 1:
                    if board[i][j] == "O":
                        if [i, j] not in visited:
                            stack.append([i, j])
                            visited.append([i, j])
                        while stack:
                            curR, curC = stack.pop()
                            for h in range(4):
                                nextR = curR + dr[h]
                                nextC = curC + dc[h]
                                if 0 <= nextR < row and 0 <= nextC < col:
                                    if [nextR, nextC] not in visited and board[nextR][nextC] == "O":
                                        visited.append([nextR, nextC])
                                        stack.append([nextR, nextC])
        for i in range(row):
            for j in range(col):
                if [i, j] not in visited:
                    if board[i][j] == "O":
                        board[i][j] = "X"


# @lc code=end
