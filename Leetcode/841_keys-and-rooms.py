#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#


# @lc code=start
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        record = set()
        visited = [0 for _ in range(len(rooms))]
        visited[0] = 1

        for key in rooms[0]:
            record.add(key)

        while record:
            ele = record.pop()
            if not visited[ele]:
                visited[ele] = 1
                for key in rooms[ele]:
                    record.add(key)

        if 0 in visited:
            return False
        else:
            return True


# @lc code=end
