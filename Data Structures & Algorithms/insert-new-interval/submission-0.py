import bisect
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        # all(elem < x for elem in a[:ip]) and all(elem >= x for elem in a[ip:])
        # Get the position of the first interval that MAY overlap with the new interval
        position_left = bisect.bisect_left(intervals, newInterval[0], key=lambda x: x[1])
        if position_left >= len(intervals):
            intervals.append(newInterval)
            return intervals

        # CASE 1 There is no overlap:
        if intervals[position_left][0] > newInterval[1]:
            return intervals[:position_left] + [newInterval] + intervals[position_left:]

        # CASE 1 There is a leftmost overlap:
        # Let's find the rightmost overlap:
        # Get the position of the last interval that MAY overlap with the new interval
        position_right = bisect.bisect_right(intervals, newInterval[1], key=lambda x: x[0])

        newInterval = [min(intervals[position_left][0], newInterval[0]), max(intervals[position_right - 1][1], newInterval[1])]
        return intervals[:position_left] + [newInterval] + intervals[position_right:]
