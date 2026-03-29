class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        def coins(l, i, r):
            coins = nums[i]
            coins *= 1 if l == 0 else nums[l-1]
            coins *= 1 if r == len(nums) - 1 else nums[r + 1]
            return coins

        memo = {}
        def dfs(l, r):
            if r < l:
                return 1

            if (l, r) in memo:
                return memo[(l, r)]

            if l == r:
                memo[(l, l)] = coins(l, l, l)
                print((l, l), memo[(l, l)])
                return coins(l, l, l)
            maxCoins = max(coins(l,l,r) + dfs(l+1, r), coins(l, r, r) + dfs(l, r-1))
            for i in range(l+1, r):
                maxCoins = max(maxCoins, dfs(l, i-1) + dfs(i+1, r) + coins(l, i, r))

            memo[(l, r)] = maxCoins
            print((l, r), maxCoins)
            return maxCoins

        return dfs(0, len(nums) - 1)

