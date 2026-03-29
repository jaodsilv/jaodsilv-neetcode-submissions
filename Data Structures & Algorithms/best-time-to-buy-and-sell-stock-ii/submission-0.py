class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(day: int) -> int:
            if day in memo:
                return memo[day]
            if day == len(prices):
                return 0
            profit = 0
            # Choose a day to buy
            # Today
            buy = prices[day]
            # Choose a day to sell
            for i in range(day+1, len(prices)):
                sell = prices[i]
                if sell > buy:
                    profit = max(profit, sell - buy + dfs(i+1))
            memo[day] = max(profit, dfs(day+1))
            return memo[day]
            # We can 
        return dfs(0)


