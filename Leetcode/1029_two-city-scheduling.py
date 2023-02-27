#
# @lc app=leetcode id=1029 lang=python3
#
# [1029] Two City Scheduling
#

# @lc code=start


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        N = len(costs) // 2
        refund = []
        result = 0
        for i in range(N):
            refund.append(costs[i][1] - costs[i][0])
            result += costs[i][0]
        refund.sort()
        for i in range(N):
            result += refund[i]
        return result


# @lc code=end
