class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        DP
            0 1 2
            a a -
        0 . F F F
        1 b F F F
        2 - F F T

             0 1 2 3
             n n n -
        0 n* T T T F
        1 -  F F F T

             0 1 2 3
             x y z -
        0 .* T T T F
        0 z  F F T F
        1 -  F F F T

             0 1 2
             a b -
        0 .* F F F
        0 c  F F F
        1 -  F F T

             0 1 2 3
             a a -
        0 a  T T F
        0 b* T T T
        1 -  F F T
        2 - 

        '''
        p2 = []
        i = 0
        while i < len(p)-1:
            if p[i+1] == '*':
                p2.append(p[i:i+2])
                i += 2
            else:
                p2.append(p[i])
                i += 1
        if i == len(p)-1:
            p2.append(p[i])

        print(p2)
        dp = [[False]*(len(s) + 1) for _ in p2]
        dp.append([False]*len(s) + [True])

        print(dp)
        for i in range(len(p2)-1, -1, -1):
            if len(p2[i]) == 2:
                dp[i][-1] = dp[i+1][-1]
            for j in range(len(s)-1,-1,-1):
                print(0, i, j, p2[i], s[j])
                if s[j] == p2[i] or p2[i] == '.':
                    # Required to take as a positive match:
                    dp[i][j] = dp[i+1][j+1]
                elif p2[i] == '.*' or p2[i][0] == s[j]:
                    dp[i][j] = dp[i+1][j+1] or dp[i+1][j] or dp[i][j+1]
                elif len(p2[i]) == 2:
                    dp[i][j] = dp[i+1][j]
                print(dp[i][j])
                # else dp[i][j] = False
        print(dp)
        return dp[0][0]
    def isMatch_DPTopDown(self, s: str, p: str) -> bool:
        memo = set()
        p2 = []
        i = 0
        while i < len(p)-1:
            if p[i+1] == '*':
                p2.append(p[i:i+2])
                i += 2
            else:
                p2.append(p[i])
                i += 1
        if i == len(p)-1:
            p2.append(p[i])
        
        # Easiest optimal solution is memoization with backtracking/DFS (a.k.a. DP top-down)
        i = 0
        while i < min(len(s), len(p2)) and (s[i] == p2[i] or p2[i] == '.'):
            i += 1

        s = s[i:]
        p2 = p2[i:]

        i, j = len(s)-1, len(p2)-1
        while i >= 0 and j >= 0 and (s[i] == p2[j] or p2[j] == '.'):
            i -= 1
            j -= 1
        s = s[:i+1]
        p2 = p2[:j+1]

        if len(p2) == 0:
            return len(s) == 0
        if len(s) == 0:
            for t in p2:
                if len(t) != 2:
                    return False
            return True

        def dfs(i, j):
            '''
            i is the index in s
            j is the index in p2
            '''
            if (i, j) in memo:
                return False
            memo.add((i, j))
            if i >= len(s):
                for t in p2[j:]:
                    if len(t) != 2:
                        return False
                return True
            if j >= len(p2):
                return False
            if len(p2[j]) == 2: # Something *
                if dfs(i, j+1):
                    return True
                while i < len(s) and (s[i] == p2[j][0] or p2[j][0] == '.'):
                    i += 1
                    if dfs(i, j):
                        return True
                return False
            return (p2[j] == s[i] or p2[j] == '.') and dfs(i+1, j+1)
        return dfs(0,0)