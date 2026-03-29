class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        maxProfit = 0
        while i < len(prices) - 1:
            # First we try to find the next local minimum for i:
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1
            print("i", i)
            j = i + 1
            while j < len(prices):
                # Now we try to find the next local maximum
                while j < len(prices) - 1 and prices[j] < prices[j + 1]:
                    j += 1

                print("j", j)
                if j < len(prices) and prices[j] - prices[i] > maxProfit:
                    maxProfit = prices[j] - prices[i]
                j += 1
            i += 1
        return maxProfit