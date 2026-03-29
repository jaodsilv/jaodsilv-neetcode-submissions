class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0
        if len(t) == len(s):
            return 1 if t == s else 0
        '''
        s="caaat"
        t="cat"
            c a a a t       
        c [ 3 0 0 0 0 0]
        a [ 3 3 2 1 0 0]
        t [ 1 1 1 1 1 0]
          [ 1 1 1 1 1 1]
        '''
        # We certainly need a DP to improve this
        # There are many repeated states
        # How to represent those repeated states
        dp = [[0]*(len(s)+1) for _ in range(len(t))]
        dp.append([1]*(len(s)+1))
        # Representing the number of possibilities to form using the remaining of t and s
        for i in range(len(t)-1, -1, -1):
            for j in range(len(s)-1, -1, -1):
                if s[j] == t[i]:
                    dp[i][j] = dp[i+1][j+1] + dp[i][j+1]
                else:
                    dp[i][j] = dp[i][j+1]
                
        return dp[0][0]
