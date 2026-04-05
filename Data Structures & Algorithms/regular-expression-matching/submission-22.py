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
        
        dpPrev = None
        dp = [False]*m + [True]
        for i in range(m-1, -1, -1):
            if len(pp[i]) == 2:
                dp[i] = True
            else:
                break

        for j in range(n-1, -1, -1):
            dpPrev = dp
            dp = [False]*(m+1)
            for i in range(m-1, -1, -1):
                if pp[i] == s[j] or pp[i] == '.':
                    dp[i] = dpPrev[i+1]
                else:
                    res = False
                    if len(pp[i]) == 2:
                        res = dp[i+1]
                    if pp[i][0] == '.' or pp[i][0] == s[j]:
                        res |= dpPrev[i+1] or dpPrev[i]
                    dp[i] = res

        return dp[0]