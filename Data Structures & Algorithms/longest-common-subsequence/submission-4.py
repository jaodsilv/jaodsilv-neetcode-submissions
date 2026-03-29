class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) == 1:
            return 1 if text1[0] in text2 else 0
        if len(text2) == 1:
            return 1 if text2[0] in text1 else 0

        '''
          p s n w
        v[4 3 2 1 0]
        o[3 3 2 1 0]
        z[3 1 0 0 0]
        s[1 1 0 0 0]
        h[0 0 0 0 0]
        -[0 0 0 0 0]
        '''
        if len(text1) > len(text2):
            text1, text2 = text2, text1
        dp = [0]*(len(text1) + 1) # O(min(len(text1), len(text2))) space

        for i in range(len(text2)-1, -1, -1):  # O(max(len(text1), len(text2)))*O(min(len(text1),len(text2)) = O(mn) Time
            dpPrev = dp
            dp = [0]*(len(text1) + 1) # O(min(len(text1), len(text2))) space

            for j in range(len(text1)-1, -1, -1): # O(min(text1, text2))
                if text1[j] == text2[i]:
                    dp[j] = dpPrev[j+1] + 1
                else:
                    dp[j] = max(dpPrev[j], dp[j+1])
        return dp[0]