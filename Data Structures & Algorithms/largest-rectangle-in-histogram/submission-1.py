import heapq

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1:
            return heights[0]

        '''
        Take the first element
        7
        store as max height and add it to a stack
        take the second element
        
        [7] => (7, 0)

        [7,1] => 7*(1-0) (pop), (1, 1)

        [7, 1, 7] => (7) (1,3), (7)
        [7, 1, 7, 2] => (7) 1*4, 7*1 (POP), 2*2
        [7, 1, 7, 2, 2] => (7) 1*5, 2*3, 2*3
        [7, 1, 7, 2, 2, 4] => (7) 1*6, 

        Take 1

        1, 3 we have 1*2 or 3*1

        1, 3, 7 we have [1*3, 3*2, 7*1]

        We have to store the begin and find the end of each.
        The end will come first to those who are bigger
        '''
        maxArea = heights[0]
        stack = []
        for i, height in enumerate(heights):
            if not stack:
                stack.append((height, 0))
            else:
                minIndex = stack[-1][1]
                if stack[-1][0] > height:
                    # If decreasing, we need to close the biggest, and convert it to the hight of the smaller
                    while stack and stack[-1][0] > height:
                        closing = stack.pop()
                        maxArea = max(maxArea, closing[0]*(i - closing[1]))
                        minIndex = closing[1]
                    if not stack or stack[-1][0] < height:
                        stack.append((height, minIndex))
                elif stack[-1][0] < height:
                    stack.append((height, i))
                # else: Same size we just ignore.
            print(maxArea, stack)
        # Close all remaining
        while stack:
            next = stack.pop()
            maxArea = max(maxArea, next[0]*(len(heights) - next[1]))
            print(maxArea, stack)
        return maxArea

