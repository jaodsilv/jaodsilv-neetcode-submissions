INF = 1001

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        '''
          [  1  2  4 - - - ]
        B    3  2 -4 0 0 0
        S    4  4  4 0 0 0
        '''
        dpB = [0]*(len(prices)+2)
        dpS = [0]*(len(prices)+1)
        for i in range(len(prices)-1, -1, -1):
            dpS[i] = max(dpS[i+1], dpB[i+2] + prices[i])
            dpB[i] = max(dpS[i+1] - prices[i], dpB[i+1])

        return dpB[0] if dpB[0] > 0 else 0

        memo = {}
        def dfs(day: int, buy: bool) -> int:
            # max profit starting from this day.
            if (day, buy) in memo:
                return memo[(day, buy)]
            
            if day >= len(prices):
                return 0

            maxBalance = 0
            for i in range(day, len(memo)):
                currBalance = 0
                if buy:
                    # What happens when we buy on day i
                    currBalance = dfs(i+1, False) - prices[i]
                else:
                    # What happens when we sell on day i
                    currBalance = dfs(i+2, True) + prices[i]
                maxBalance = max(maxBalance, currBalance)
            memo[(day, buy)] = maxBalance
            return maxBalance
        return dfs(0, True)
