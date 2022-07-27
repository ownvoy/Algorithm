from collections import deque


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        queue = deque()
        amounts = {}
        if amount == 0:
            return 0
        for coin in coins:
            queue.append(coin)
            amounts[coin] = 1
            if amount == coin:
                return amounts[coin]
        count = 1
        while queue and count < 1000000:
            current = queue.popleft()
            for coin in coins:
                nextC = current + coin
                if nextC not in amounts:
                    amounts[nextC] = amounts[current] + 1
                    queue.append(nextC)
                    count += 1
                if nextC == amount:
                    return amounts[nextC]
        return -1


solution1 = Solution()
solution2 = Solution()
solution3 = Solution()

print(solution1.coinChange([1, 2, 5], 11))
print(solution2.coinChange(coins=[2], amount=3))
print(solution3.coinChange(coins=[1], amount=0))
