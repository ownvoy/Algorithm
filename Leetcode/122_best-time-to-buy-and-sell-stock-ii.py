#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        first = 0
        partial = 0
        for i in range(0, len(prices) - 1):
            if prices[i + 1] - prices[i] > 0:
                partial = max(partial, prices[i + 1] - prices[first])
            else:
                profit += partial
                partial = 0
                first = i + 1
        profit += partial
        return profit


# @lc code=end
