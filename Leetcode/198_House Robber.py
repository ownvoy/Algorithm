class Solution:
    def __init__(self):
        self.result = {}
    def maxCostClimbingStairs(self, cost: list[int]) -> int:
        goal = len(cost)
        if goal == 1:
            return cost[0]
        elif goal == 2:
            return  max(cost[0],cost[1])
        elif goal == 3:
            return max(cost[0]+cost[2],cost[1])
        else:
            self.result[0] = cost[0]
            self.result[1] = max(cost[0],cost[1])
            self.result[2] = max(cost[0]+cost[2],cost[1])
            temp1 = self.maxCostCalculate(cost, goal-1)
            temp2 = self.maxCostCalculate(cost, goal-2)
            return max(temp1, temp2)
    def maxCostCalculate(self,cost, goal):
        if goal == 0:
            return self.result[0]
        elif goal == 1:
            return self.result[1]
        elif goal == 2:
            return self.result[2]
        else:
            if goal not in self.result:
                self.result[goal]= cost[goal]+max(self.maxCostCalculate(cost, goal-2),
                                                self.maxCostCalculate(cost, goal-3))
            return self.result[goal]
            
solution = Solution()
answer =solution.maxCostClimbingStairs([2,7,9,3,1])
print(answer)