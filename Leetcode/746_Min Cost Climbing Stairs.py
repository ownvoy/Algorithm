class Solution:
    def __init__(self):
        self.result = {}
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        goal = len(cost)
        
        if goal == 1:
            return cost[0]
        elif goal == 2:
            return  cost[1]
        else:
            self.result[0] = cost[0]
            self.result[1] = cost[1]
            temp1 = self.minCostCalculate(cost, goal-1)
            temp2 = self.minCostCalculate(cost, goal-2)
            return min(temp1, temp2)
    def minCostCalculate(self,cost, goal):
        if goal == 0:
            return self.result[0]
        elif goal == 1:
            return self.result[1]
        else:
            if goal not in self.result:
                self.result[goal]= cost[goal]+ min(self.minCostCalculate(cost, goal-1),
                                                                                    self.minCostCalculate(cost, goal-2))
            return self.result[goal]
            
solution = Solution()
answer =solution.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1])
print(answer)
