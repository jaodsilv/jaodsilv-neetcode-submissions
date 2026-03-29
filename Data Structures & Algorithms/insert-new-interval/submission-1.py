import bisect
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Solution 1:
        '''
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
        '''


        # Solution 2:
        def generator(newInterval):
            yielded = False
            for i in range(len(intervals)):
                if intervals[i][1] < newInterval[0]:
                    yield intervals[i]
                elif intervals[i][0] <= newInterval[1]: # and intervals[i][1] >= newInterval[0]
                    newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
                elif not yielded:
                    yield newInterval
                    yield intervals[i]
                    yielded = True
                else:
                    yield intervals[i]
            if not yielded:
                yield newInterval
        return list(generator(newInterval))

