#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def __init__(self):
        self.result = [[1], [1,1]]
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return self.result
        while len(self.result) < numRows:
            new = []
            for i in range(0,len(self.result[-1])-1):
                new.append(self.result[-1][i] + self.result[-1][i+1])
            self.result.append(list([1] + new + [1]))
        return self.result
# @lc code=end

