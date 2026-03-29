"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Let's first sort the intervals
        intervals.sort(key=lambda x: x.start)
        #print(intervals)
        ends = []
        heapq.heapify(ends)
        for interval in intervals:
            if len(ends) == 0:
                heapq.heappush(ends, interval.end)
            else:
                if interval.start >= ends[0]:
                    heapq.heapreplace(ends, interval.end)
                else:
                    heapq.heappush(ends, interval.end)
        return len(ends)
