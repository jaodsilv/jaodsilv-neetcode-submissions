class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        coins = [i for i in coins if i <= amount]
        dp = [0]*amount + [1]
        dpPrev = [0]*amount + [1]
        # Representing the number of possible ways to get the amount when we already have i
        # considering only the coins to the right of coins[j]
        for i in range(len(coins)-1, -1, -1):
            for j in range(amount-1, -1, -1):
                dp[j] = dpPrev[j]
                if j + coins[i] <= amount:
                    dp[j] += dp[j + coins[i]]
            dpPrev = dp
            print(dp)
            dp = [0]*amount + [1]
            
        return dpPrev[0]
'''
   0  1  2  3  4
1 [4, 3, 2, 1, 1]
2 [1, 1, 1, 0, 1]
3 [0, 1, 0, 0, 1]
- [0, 0, 0, 0, 1]

'''
