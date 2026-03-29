class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        DP =[0]*len(prices)
        '''
        Representing the maximum profit buying at day i or later
        last 2 days are surely to be 0 due to the cooldown

        [1,3,4,0,4]
        given a state:
        [3,1,0,0,0]
        '''

        memo = {}
        def dfs(i, sell):
            if (i, sell) in memo:
                return memo[(i, sell)]
            if i >= len(prices):
                return 0
            currPrice = prices[i]
            profit = 0
            if sell:
                # Meaning we bought on day i
                for j in range(i+1, len(prices)):
                    p = prices[j]
                    if p > currPrice:
                        profit = max(profit, p - currPrice + dfs(j + 2, False))
            else:
                # Meaning we sold on i - 2 or never sold
                for j in range(i, len(prices) - 1):
                    p = prices[j]
                    profit = max(profit, dfs(j, True))
            memo[(i, sell)] = profit
            return profit
            

        return dfs(0, False)