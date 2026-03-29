
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return nums[0]*nums[1] + max(nums)

        memo = {}

        def dfs(l: int, r :int, memo: dict) -> int:
            if l > r:
                return 0

            if (l, r) in memo:
                return memo[(l, r)]

            maxCoins = 0
            for i in range(l, r+1):
                coins = nums[i]
                if l > 0:
                    coins *= nums[l-1]
                if r < len(nums) - 1:
                    coins *= nums[r+1]
                coins += dfs(l, i-1, memo) + dfs(i+1, r, memo)
                maxCoins = max(maxCoins, coins)
            memo[(l, r)] = maxCoins
            return maxCoins
        return dfs(0, len(nums) - 1, memo)
