# @before-stub-for-debug-begin
from python3problem55 import *
from typing import *

# @before-stub-for-debug-end

#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= last:
                last = i
        if last == 0:
            return True


# @lc code=end
