#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sort = sorted(nums)
        start_idx = 0
        end_idx = len(nums)-1
        while start_idx != end_idx:
            sum = sort[start_idx] + sort[end_idx]
            if sum == target:
                idx1 = nums.index(sort[start_idx])
                idx2 = nums.index(sort[end_idx])
                if idx1 == idx2:
                    rest_list = list(
                        filter(lambda x: nums[x] == sort[start_idx], range(len(nums))))
                    return rest_list
                return [idx1, idx2]
            elif sum > target:
                end_idx -= 1
            else:
                start_idx += 1
# @lc code=end
