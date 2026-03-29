class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) == 0:
            return s2 == s3
        if len(s2) == 0:
            return s1 == s3
        if len(s3) != len(s1) + len(s2):
            return False

        '''
        dp
           a  a  a  a  -
        b[aT,aT,bT,bF,bF]
        b[aF,bF,bT,bF,bF]
        b[bF,bF,bT,bF,aF]
        b[bF,bF,bT,aF,aF]
        -[bF,bF,aT,aT,-T]
        
          aabbbbaa

          a  b  c  -
        x[F, F, F, F]
        y[F, F, F, F]
        z[F, F, F, F]
        -[F, F, F, T]
         abxzcy"
        '''
        if len(s1) > len(s2):
            s1, s2 = s2, s1
        dp = [False]*len(s1) + [True]
        i = len(s1) - 1
        while i >= 0 and s1[i] == s3[len(s2) + i]:
            dp[i] = True
            i -= 1
        print(dp)
        lastT = len(s1)
        for i in range(len(s2)-1, -1, -1):
            dpPrev = dp
            dp = [False]*(len(s1)+1)
            j = lastT
            if dpPrev[-1] and s2[i] == s3[i+len(s1)]:
                dp[-1] = True
            for j in range(len(s1)-1, -1, -1):
                dp[j] = (dpPrev[j] and s2[i] == s3[i+j]) or (dp[j+1] and s1[j] == s3[i+j])
            print(dp)
        return dp[0]