#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums) -> int:
        maxsum = nums[0]
        cursum = 0
        for num in nums:
            if cursum < 0:
                cursum = 0
            cursum += num
            maxsum = max(maxsum, cursum)
        return maxsum


# @lc code=end
