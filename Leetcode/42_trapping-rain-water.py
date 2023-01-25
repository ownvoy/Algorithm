#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        wall = sum(height)
        left = 0
        right = len(height) - 1
        result = 0
        level = 0
        while left != right:
            if level < min(height[left], height[right]):
                fill = min(height[left], height[right]) - level
                level = min(height[left], height[right])
                result += (right - left + 1) * fill
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        mmax = max(height)
        mmax_count = height.count(mmax)
        if mmax_count != 1:
            pass
        else:
            for _ in range(mmax_count):
                height.remove(mmax)
            if len(height) == 0:
                return 0
            second_max = max(height)
            var = mmax - second_max
            result += mmax_count * var
        result -= wall
        return result


# @lc code=end
