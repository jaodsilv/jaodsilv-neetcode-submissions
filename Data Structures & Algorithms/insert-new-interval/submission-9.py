class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        Let's find with binary search the insertion point separetely for left and for right indexes
        '''
        if len(intervals) == 0:
            return [newInterval]

        def find(value, index):
            left = 0
            right = len(intervals)
            while right - left > 1:
                mid = (right + left) >> 1
                print("left, right, mid", left, right, mid)

                # Value is between two intervals
                if intervals[mid][1] < value and (mid >= len(intervals) - 1 or intervals[mid + 1][0] > value):
                    # Add + 1 if we are looking the start value
                    return mid + (index ^ 1)
                
                # Value is within an interval
                if intervals[mid][0] <= value and intervals[mid][1] >= value:
                    return mid
                
                # Value is entirely to the left of mid
                if intervals[mid][0] > value:
                    right = mid
                # Value is entirely to the right of mid
                else: # if intervals[mid][1] <= value
                    left = mid
            return (right + left) >> 1

        def hasOverlap(a, b):
            return (a[0] >= b[0] and a[0] <= b[1]) or (a[1] >= b[0] and a[1] <= b[1]) or (a[0] <= b[0] and a[1] >= b[1]) or (a[0] >= b[0] and a[1] <= b[1])

        # It is totally to left:
        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals
        # It is totally to right:
        if newInterval[0] > intervals[-1][1]:
            return intervals + [newInterval]

        left = find(newInterval[0], 0)
        print("result L", left)
        right = find(newInterval[1], 1)
        print("result R", right)

        if right < left:
            return intervals[:left] + [newInterval] + intervals[left:]

        # We must test if there is an overlap
        # has Overlap on the left:
        # if newInterval[1] < intervals[left][0] or newInterval[0] > intervals[left][1]:
            # print("newInterval[1] < intervals[left][0] or newInterval[0] > intervals[right][1]")
            # return intervals[:left] + [newInterval] + intervals[right:]

        # It is totally to the left or It is totally to the right
        # It Overlaps on its left
        if left < len(intervals) and hasOverlap(newInterval, intervals[left]):
            newInterval = [min(intervals[left][0], newInterval[0]), max(intervals[left][1], newInterval[1])]
        else:
            left += 1

        if right < len(intervals) and hasOverlap(newInterval, intervals[right]):
            newInterval = [min(intervals[right][0], newInterval[0]), max(intervals[right][1], newInterval[1])]
            right += 1

        print("left, right", left, right)
        if right >= len(intervals):
            return intervals[:left] + [newInterval]
        else:
            return intervals[:left] + [newInterval] + intervals[right:]
