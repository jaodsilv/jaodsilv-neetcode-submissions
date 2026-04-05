class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Let's map each char to a compressed index
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        m = len(text1)
        n = len(text2)
        dpPrev = None
        dp = [0] * (n + 1)
        for i in range(m-1, -1, -1):
            dpPrev = dp
            dp = [0] * (n + 1)
            for j in range(n-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[j] = 1 + dpPrev[j+1]
                else:
                    dp[j] = max(dp[j+1], dpPrev[j], dpPrev[j+1])
        return dp[0]
