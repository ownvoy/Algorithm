#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        p = 0
        f = len(height) - 1
        while f > p:
            weight = f - p
            y = min(height[f], height[p])
            area = weight * y
            result = max(result, area)
            if y == height[f]:
                f -= 1
            else:
                p += 1
        return result


# @lc code=end
