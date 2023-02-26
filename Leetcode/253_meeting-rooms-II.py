from heapq import heappop, heappush


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        endlist = []

        intervals.sort(key=lambda x: x[0])
        for interval in intervals:
            start, end = interval
            if endlist and endlist[0] <= start:
                heappop(endlist)
                heappush(endlist, end)
            else:
                heappush(endlist, end)
        return len(endlist)
