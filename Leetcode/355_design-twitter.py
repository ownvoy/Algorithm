#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#

# @lc code=start
from heapq import heappush, heappop


class Twitter:
    def __init__(self):
        self.time = 1
        self.userMap = {}
        for user in range(1, 501):
            self.userHistory[user] = []
        self.followMap = [[i] for i in range(0, 501)]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userHistory[userId].append([-self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        for user in self.followMap[userId]:
            heappush(heap, self.userHistory[user])
        result = []
        count = 0
        while heap and count < 10:
            result.append(heappop(heap))
            count += 1
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end
