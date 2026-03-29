class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        memo = {}
        def dfs(L, R):
            if (L,R) in memo:
                return memo[(L, R)]
            if L > R:
                return 0
            if L == R:
                memo[(L,L)] = nums[L]*nums[L-1]*nums[L+1]
                return memo[(L, L)]
            borders = nums[L-1]*nums[R+1]
            res = 0
            for i in range(L, R+1):
                res = max(res, dfs(L, i-1) + dfs(i+1, R) + borders*nums[i])
            memo[(L,R)] = res
            return res
        return dfs(1, len(nums)-2)
