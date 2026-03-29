"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Let's first sort the intervals
        intervals.sort(key=lambda x: x.start)
        remaining = []
        days = 0
        lastEnd = 0
        while intervals:
            #print(intervals)
            days += 1
            for interval in intervals:
                if interval.start < lastEnd:
                    remaining.append(interval)
                else:
                    lastEnd = interval.end
            intervals = remaining
            lastEnd = 0
            remaining = []
        return days
