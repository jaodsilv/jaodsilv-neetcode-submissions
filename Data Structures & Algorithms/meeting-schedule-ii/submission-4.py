import heapq

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) <= 1:
            return len(intervals)

        intervals.sort(key=lambda x: x.start)

        dayslast = []
        for interval in intervals:
            if dayslast and dayslast[0] <= interval.start:
                heapq.heapreplace(dayslast, interval.end)
            else:
                heapq.heappush(dayslast, interval.end)
        return len(dayslast)
