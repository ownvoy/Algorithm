#
# @lc app=leetcode id=2244 lang=python3
#
# [2244] Minimum Rounds to Complete All Tasks
#

# @lc code=start
class Solution:
    def __init__(self):
        self.numdict = {}
        self.numdict[0] = 0
        self.numdict[1] = float("inf")
        self.numdict[2] = 1
        self.numdict[3] = 1

    def minimumRounds(self, tasks: List[int]) -> int:
        countdict = {}
        for task in tasks:
            countdict[task] = 1 + countdict.get(task, 0)
        result = 0
        print(countdict.values())
        for count in countdict.values():
            temp = min(1 + self.topdown(count - 2), 1 + self.topdown(count - 3))
            result += temp
            if temp == float("inf"):
                return -1
        return result

    def topdown(self, num):
        if num < 0:
            return float("inf")

        if num in self.numdict:
            return self.numdict[num]
        else:
            self.numdict[num] = 1 + min(self.topdown(num - 2), self.topdown(num - 3))
            return self.numdict[num]


# @lc code=end
