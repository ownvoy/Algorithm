#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#

# @lc code=start
from heapq import heapify, heappush, heappop


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapify(self.heap)
        while len(self.heap) > self.k:
            heappop(self.heap)
        while len(self.heap) < self.k:
            heappush(self.heap, -1000000)

    def add(self, val: int) -> int:
        heappush(self.heap, val)
        if len(self.heap) == 1:
            return self.heap[0]
        heappop(self.heap)
        if self.heap[0] == -1000000:

            return None
        else:
            return self.heap[0]


# Your KthLargest object will be instantiated and called as such:

# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end
