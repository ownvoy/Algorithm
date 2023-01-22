# @before-stub-for-debug-begin
from typing import *

from python3problem3 import *

# @before-stub-for-debug-end

#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        long = [0]
        substring = ''
        while i <= len(s)-1:
            if s[i] not in substring:
                substring += s[i]
                i += 1
                long.append(len(substring))
            else:
                long.append(len(substring))
                substring += s[i]
                re_idx = substring.index(s[i])
                substring = substring[re_idx+1:]
                i += 1
        return max(long)
# @lc code=end
