class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1

        dp = [0]*amount + [1]
        dpPrev = [0]*amount + [1]

        # DP where (i, j) is count of ways to reach amount from i with coins after the j-th coin
        # coins.sort()

        '''
           99 1 
        0 [ 0 0 0]
        1 [ 0 0 0]
        2 [ 0 0 0]
        3 [ 0 1 0]
        4 [ 1 1 1]
        '''

        for j in range(len(coins) - 1, -1, -1):
            for i in range(amount - 1, -1, -1):
                if i + coins[j] > amount:
                    dp[i] = dpPrev[i]
                else:
                    dp[i] = dpPrev[i] + dp[i+coins[j]]
            dpPrev = dp
            dp = [0]*amount + [1]
        return dpPrev[0]