class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Find local mins and local maxes
        i = 0
        profit = 0
        while i < len(prices) - 1:
            while i < len(prices)-1 and prices[i] >= prices[i+1]:
                i += 1
            if i == len(prices) - 1:
                break
            profit -= prices[i]

            i += 1

            while i < len(prices) - 1 and prices[i] <= prices[i+1]:
                i+=1
            profit += prices[i]
            i += 1
        return profit
