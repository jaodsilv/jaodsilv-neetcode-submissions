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
            found = False
            for i in range(len(dayslast)):
                last = dayslast[i]
                if last <= interval.start:
                    dayslast[i] = interval.end
                    found = True
                    break
            if not found:
                dayslast.append(interval.end)
        return len(dayslast)
