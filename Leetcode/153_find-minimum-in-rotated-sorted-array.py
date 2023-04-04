#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        result = nums[0]
        while l <= r:
            mid = (l + r) // 2
            if nums[l] < nums[mid]:
                l = mid + 1
                result = min(result, nums[l])
            elif nums[r] > nums[mid]:
                r = mid - 1
        return result


# @lc code=end
