# @before-stub-for-debug-begin
from python3problem347 import *
from typing import *

# @before-stub-for-debug-end

#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        result = []
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        sl = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
        for i in range(0, k):
            result.append(sl[i][0])
        return result


# @lc code=end
