# @before-stub-for-debug-begin
from python3problem242 import *
from typing import *

# @before-stub-for-debug-end

#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        return sorted_s == sorted_t


# @lc code=end
