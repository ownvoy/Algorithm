# @before-stub-for-debug-begin
# from typing import *

# from python3problem344 import *

# @before-stub-for-debug-end

#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
class Solution(object):
    def reverseString(self, s):
        l = len(s)
        if l == 1:
            return s
        elif l ==2:
            return list(s[1] + s[0])
        else:
            return list(s[l-1])+self.reverseString(s[1:l-1])+list(s[0])
# @lc code=end

solution = Solution()
print(solution.reverseString(s = ["h","e","l","l","o"]))

