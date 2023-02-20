#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix) - 1
        col = len(matrix[0]) - 1
        start = [0, 0]
        end = [row, col]
        while start[0] < end[0]:
            mid = [(start[0] + end[0]) // 2, (start[1] + end[1]) // 2]
            if matrix[mid[0]][mid[1]] == target:
                return True
            elif matrix[mid[0]][mid[1]] > target:
                end[0] -= 1
            else:
                start[0] += 1
        while start[1] <= end[1]:
            mid = [(start[0] + end[0]) // 2, (start[1] + end[1]) // 2]

            if matrix[mid[0]][mid[1]] == target:
                return True
            elif matrix[mid[0]][mid[1]] > target:
                end[1] -= 1
            else:
                start[1] += 1
        return True


# @lc code=end
