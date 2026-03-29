
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return nums[0]*nums[1] + max(nums)

        # def dfs(l: int, r :int, memo: dict) -> int:
        #     if l > r:
        #         return 0

        #     if (l, r) in memo:
        #         return memo[(l, r)]

        #     maxCoins = 0
        #     for i in range(l, r+1):
        #     memo[(l, r)] = maxCoins
        #     return maxCoins

        nums = [1] + nums + [1] # l, r range from 1 to n - 2
        n = len(nums)
        dp = [[0]*(n) for _ in range(n)]
        for l in range(n - 2, 0, -1):
            for r in range(l, n-1):
                maxCoins = 0
                for i in range(l, r + 1):
                    coins = nums[i]*nums[l-1]* nums[r+1]
                    coins += dp[l][i-1] + dp[i+1][r]
                    maxCoins = max(maxCoins, coins)
                dp[l][r] = maxCoins
        print(dp)
        return dp[1][-2]
