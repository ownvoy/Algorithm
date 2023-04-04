# @before-stub-for-debug-begin
from typing import *

from python3problem394 import *

# @before-stub-for-debug-end

#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        num = ['0','1','2','3','4','5','6','7','8','9']
        for i in range(len(s)): 
            if s[i] == "[" :
                stack = []
                flag = 0
                for k in range(i+1,len(s)):
                    if s[k] == "[":
                        stack.append(s[k])
                        flag += 1
                    elif s[k] == "]" and flag == 0:
                        sub = "".join(stack)
                        multiple = ""
                        idx = 0
                        for p in reversed(range(i)):
                            if s[p] in num:
                                multiple += s[p]
                                idx = p
                            else:
                                break
                        return s[:idx]+ int(multiple[::-1]) * self.decodeString(sub) +self.decodeString(s[k+1:])
                    elif s[k] == "]" and flag != 0:
                        stack.append(s[k])
                        flag -= 1
                    else:
                        stack.append(s[k])
        return s
        
# @lc code=end

