class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = [[0]*len(nums) for _ in range(len(nums))]
        for i in range(1, len(nums)-1):
            for j in range(i, 0, -1):
                p = nums[j-1]*nums[i+1]
                dp[i][j] = max(p*nums[j] + dp[i][j+1], p*nums[i] + dp[i-1][j])
                for k in range(j, i+1):
                    dp[i][j] = max(dp[i][j], p*nums[k] + dp[k-1][j] + dp[i][k+1])

        print(dp)
        return dp[-2][1]

        '''
          0 1   2   3   4   5
        0 0 0   0   0   0   0
        1 0 8   0   0   0   0
        2 0 12  24  0   0   0
        3 0 28  84  42  0   0
        4 0 7   28  14  21  0
        5 0 0   0   0   0   0
          0 0   0   0   0   0
          0 8   0   0   0   0
          0 36  24  0   0   0
          0 64  108 42  0   0
          0 24  57  56  21  0
          0 0   0   0   0   0]]
           0   1    2   3   4   5
           1   4    2   3   7   1
        0 1 ?   0    0   0   0   0
        1 4 0   8    0   0   0   0
        2 2 0  36   24   0   0   0 dp[2][1] = max(dp[1][1]+nums[0]*nums[2]*nums[3], dp[2][2]+nums[0]*nums[1]*nums[3])
        3 3 0 136 -108- 42   0   0 dp[3][2] = max(dp[2][2]+nums[1]*nums[3]*nums[4], dp[3][3]+nums[1]*nums[2]*nums[4]);
        4 7 0 143  136  56  21   0 dp[4][3] = max(dp[3][3]+nums[2]*nums[4]*nums[5], dp[4][4]+nums[2]*nums[3]*nums[5])
        5 1 0   0    0   0   0   0
        dp[3][1] = max(dp[1][1]+dp[3][2], dp[2][2]+max(nums[0]*nums[1]*nums[3]+nums[0]*nums[3]*nums[4], nums[0]*nums[1]*nums[4]+nums[1]*nums[3]*nums[4]) + nums[dp[1][1]+dp[3][3], dp[3][3]+dp[2][1]) = (116, , 78)
        '''
        # Each pair L, R is called multiple times.
        # But only once in a way to store the results. So, it does not to inner loop again
        # Therefore, The inner loop will run for each element This means it is O(n²) time.
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
            for i in range(L, R+1): # O(R-L)*
                res = max(res, dfs(L, i-1) + dfs(i+1, R) + borders*nums[i])
            memo[(L,R)] = res
            return res
        dfs(1, len(nums)-2)
        print(memo)
        return memo[(1, len(nums)-2)]
