class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Edge Cases
        if len(intervals) == 0:
            return [newInterval]

        # Brute force:
        i = 0

        while i < len(intervals) and newInterval[0] > intervals[i][1]:
            i += 1

        if i == len(intervals):
            return intervals + [newInterval]

        # Now we test the overlap in the borders
        res = intervals[:i]

        # newInterval[0] <= intervals[i][1]:
        if i < len(intervals) and newInterval[1] < intervals[i][0]:
            # No overlap
            res.append(newInterval)
            res += intervals[i:]
            return res

        left = min(newInterval[0], intervals[i][0])

        j = i
        while j < len(intervals) and newInterval[1] >= intervals[j][0]:
            j += 1

        j -= 1

        j = max(j, i)
        right = max(newInterval[1], intervals[j][1])
        res.append([left, right])
        return res + intervals[j+1:]

        

