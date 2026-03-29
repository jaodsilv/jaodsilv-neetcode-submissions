class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        coins = [i for i in coins if i <= amount]
        dp = [[0]*(len(coins)+1) for _ in range(amount)]
        dp.append([1]*(len(coins)+1))
        # Representing the number of possible ways to get the amount when we already have i
        # considering only the coins to the right of coins[j]
        for i in range(amount-1, -1, -1):
            for j in range(len(coins)-1, -1, -1):
                dp[i][j] = dp[i][j + 1]
                if i + coins[j] <= amount:
                    dp[i][j] += dp[i + coins[j]][j]
        print(dp)
        return dp[0][0]
'''
   1  2  3
0 [2, 1, 0, 0]
1 [2, 0, 1, 0]
2 [1, 1, 0, 0]
3 [1, 0, 0, 0]
4 [1, 1, 1, 1]

'''
