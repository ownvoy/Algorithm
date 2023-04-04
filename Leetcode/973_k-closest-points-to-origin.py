#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
from heapq import heappush, heappop
from math import sqrt


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        result = []
        for x, y in points:
            heappush(heap, (sqrt(x * x + y * y), [x, y]))

        while k != 0:
            result.append(heappop(heap)[1])
            k -= 1
        return result


# @lc code=end
