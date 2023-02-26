from heapq import heappop, heappush


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        result = 1
        endlist = []

        intervals.sort(key=lambda x: x[0])
        tempe = 0
        for interval in intervals:
            start, end = interval
            if tempe <= start:
                tempe = end
                heappush(endlist, tempe)
            else:
                result += 1
                print(interval)
                heappush(endlist, tempe)
                heappush(endlist, end)
            tempe = heappop(endlist)
        return result
