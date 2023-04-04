#
# @lc app=leetcode id=1328 lang=python3
#
# [1328] Break a Palindrome
#

# @lc code=start
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        length = len(palindrome)
        if length == 1:
            return ""
        mid = length // 2
        temp = list(palindrome)
        for i in range(mid):
            if temp[i] != "a":
                temp[i] = "a"
                return "".join(temp)
        temp[-1] = chr(ord(temp[-1]) + 1)
        return "".join(temp)


# @lc code=end
