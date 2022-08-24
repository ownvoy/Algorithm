class Solution:
    def __init__(self):
        self.result = {}
        self.result[1] = 1
        self.result[2] = 2
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            if n not in self.result:
                self.result[n]= self.climbStairs(n-1)+self.climbStairs(n-2)
            return self.result[n]

solution = Solution()

answer = solution.climbStairs(4)
print(answer)