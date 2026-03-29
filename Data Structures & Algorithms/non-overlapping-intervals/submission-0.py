class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Thinking on which interval to remove
        # If there is an inner interval to the other, it is clear the outer should be removed
        # The harder for multiple overlapping items.
        # let's consider the case [[1,3],[2,5],[4,7]] or [[1,5],[2,6][3,7]]
        # For that case we should consider the number of overlapping intervals to each one, and remove the one with more intervals.
        # Then, if there is a draw, we should keep the one that finishes earlier.
        #Let's start by sorting the intervals by the start of the interval
        intervals.sort(key=lambda x: x[0])
        res = []
        last = intervals[0]
        for i in intervals:
            # We know beforehand that i[0] >= last[0]
            if i[0] >= last[1]: # and i[0] >= last[0], e.g., [[0,1],[2,3]]
                res.append(last)
                last = i
            elif i[1] > last[1]: # and i[0] <= last[1] and i[0] >= last[0], e.g., [[0,3],[0,5]] or [[0,3],[1,5]]
                continue
            else: # and i[1] <= last[1] and i[0] <= last[1] and i[0] >= last[0], e.g., [[0,3],[0,2]] or [[0,3],[1,2]]
                last = i

        return len(intervals) - len(res) - 1
