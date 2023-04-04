#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#

# @lc code=start
from heapq import heappush, heappop


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heappush(heap, (-stone, stone))
        while len(heap) > 1:
            x = heappop(heap)
            y = heappop(heap)
            heappush(heap, (-x + y, x - y))
        return heap[0] if len(heap) == 1 else 0


# @lc code=end
