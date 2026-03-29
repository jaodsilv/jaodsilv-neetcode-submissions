class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        stack = []
        '''
        Prices reading back to front
        store max price found (so far)
        and maximum delta so far
        '''
        maxDelta = 0
        maxPrice = 0
        for i in prices[::-1]:
            if i > maxPrice:
                maxPrice = i
            else:
                maxDelta = max(maxDelta, maxPrice - i)
        return maxDelta