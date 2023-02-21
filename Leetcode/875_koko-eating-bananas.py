#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        result = max(piles)
        while l <= r:
            mid = (l + r) // 2
            temp = 0
            for num in piles:
                temp += ceil(num / mid)
            if h >= temp and result > mid:
                result = mid
                r = mid - 1
            else:
                l = mid + 1

        return result


# @lc code=end
