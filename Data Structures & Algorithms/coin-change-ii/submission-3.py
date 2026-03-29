class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1

        dp = [[0]*(len(coins) + 1) for _ in range(amount)]
        dp.append([1]*(len(coins) + 1))

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

        for i in range(amount - 1, -1, -1):
            for j in range(len(coins) - 1, -1, -1):
                if i + coins[j] > amount:
                    dp[i][j] = dp[i][j+1]
                else:
                    dp[i][j] = dp[i][j+1] + dp[i+coins[j]][j]
        return dp[0][0]