class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
           a -
        a  F F F
        a  T F T
        -  F T
        '''

        pp = []
        for i, c in enumerate(p):
            if c == '*':
                continue
            if i < len(p) - 1 and p[i+1] == '*':
                pp.append(c + '*')
            else:
                pp.append(c)
        
        m = len(pp)
        n = len(s)
        memo = set()

        dp = [[False]*(m+1) for _ in range(n+1)]
        dp[-1][-1] = True
        for i in range(m-1, -1, -1):
            if len(pp[i]) == 2:
                dp[-1][i] = True
            else:
                break

        for j in range(n-1, -1, -1):
            for i in range(m-1, -1, -1):
                if pp[i] == s[j] or pp[i] == '.':
                    dp[j][i] = dp[j+1][i+1]
                else:
                    res = False
                    if len(pp[i]) == 2:
                        res = dp[j][i+1]
                    if pp[i][0] == '.' or pp[i][0] == s[j]:
                        res |= dp[j+1][i+1] or dp[j+1][i]
                    dp[j][i] = res

        return dp[0][0]