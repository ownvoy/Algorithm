#
# @lc app=leetcode id=1833 lang=python3
#
# [1833] Maximum Ice Cream Bars
#

# @lc code=start
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        result = 0
        for cost in costs:
            coins -= cost
            if coins < 0:
                return result
            result += 1
        return result


# @lc code=end
