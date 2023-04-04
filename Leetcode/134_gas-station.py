#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
from collections import deque


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        start = 0
        cur = 0
        for i in range(len(gas)):
            cur += gas[i] - cost[i]
            if cur < 0:
                cur = 0
                start = i + 1
        return start


# @lc code=end
