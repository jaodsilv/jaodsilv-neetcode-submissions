class Solution:
    def numDecodings(self, s: str) -> int:
        def memoSolution():
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
            return dfs(0)

        def dpSolution():
            prevPrev = 1
            prev = 1 if s[-1] != '0' else 0
            for i in range(len(s)-2,-1,-1):
                d = int(s[i])
                if d == 0:
                    prevPrev = prev
                    prev = 0
                elif d == 1 or (d == 2 and int(s[i+1]) <= 6):
                    prev, prevPrev = prev + prevPrev, prev
                else:
                    prevPrev = prev
            return prev
        # return memoSolution()
        return dpSolution()