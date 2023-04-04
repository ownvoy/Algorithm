#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        zero_count = 0
        total = 1
        for n in nums:
            if n == 0 and zero_count == 0:
                zero_count += 1
                continue
            total = total * n
        if zero_count == 0:
            for k in range(len(nums)):
                result.append(total // nums[k])
        elif zero_count == 1:
            for k in range(len(nums)):
                if nums[k] == 0:
                    result.append(total)
                else:
                    result.append(0)
        else:
            for k in range(len(nums)):
                result.append(0)
        return result


# @lc code=end
