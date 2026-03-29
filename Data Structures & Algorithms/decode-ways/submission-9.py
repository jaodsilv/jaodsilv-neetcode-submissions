class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        memo = {}

        def dfs(i):
            if i == len(s):
                return 1
            d = int(s[i])
            if d == 0:
                return 0
            if i in memo:
                return memo[i]
            if i == len(s) - 1:
                memo[i] = 1
                return memo[i]
            
            res = 0
            if d == 1 or (d == 2 and int(s[i+1]) <= 6):
                res = dfs(i+1) + dfs(i+2)
            else:
                res = dfs(i+1)
            memo[i] = res
            return res
        dfs(0)
        print(memo)
        return memo[0]