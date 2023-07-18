#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#


# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dp(curm, curn):
            if curm == m - 1 and curn == n - 1:
                return 1

            a, b = 0, 0

            if curm != m - 1:
                a = dp(curm + 1, curn)
            if curn != n - 1:
                b = dp(curm, curn + 1)
            return sum(a, b)

        return dp(0, 0)


# @lc code=end
