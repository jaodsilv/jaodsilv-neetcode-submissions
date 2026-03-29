class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Area is defined as the height of the lowest value times the distance
        # Let`s look from the outside to the inside
        greatest = 0
        i = 0
        j = len(heights) - 1
        while i < j:
            cur = (j - i) * min(heights[j], heights[i])
            if cur > greatest:
                greatest = cur
            if heights[j] > heights[i]:
                i += 1
            elif heights[j] < heights[i]:
                j -= 1
            else:
                i += 1
                j -= 1

        return greatest