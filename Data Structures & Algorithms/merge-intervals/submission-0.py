class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        curInterval = intervals[0]
        res = []
        for interval in intervals:
            if interval[0] > curInterval[1]:
                # create a new interval
                res.append(curInterval)
                curInterval = interval
            elif interval[1] > curInterval[1]:
                curInterval[1] = interval[1]
        res.append(curInterval)
        return res