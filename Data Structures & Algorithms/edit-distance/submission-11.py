class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
           n  e  a  t  c  d  e  e  -
        n  0  0  0  0  0  0  0  7  8
        e  0  0  0  0  0  0  0  6  7
        e  4  3  3  3  4  5  4  5  6
        t  5  4  3  2  3  4  4  4  5
        c  6  5  4  3  2  3  3  3  4
        o  7  6  5  4  3  2  2  2r 3
        d  6  5  4  3  2  1a 1c 1r 2
        e  7  6  5  4  3  2r 1  0  1
        -  8  7  6  5  4  3  2  1  0
        '''
        if len(word1) > len(word2):
            word1, word2 = word2, word1

        dp = list(range(len(word1), -1, -1))

        for i in range(len(word2)-1, -1, -1):
            dpPrev = dp
            dp = [0]*len(word1) + [len(word2)-i]

            for j in range(len(word1)-1, -1, -1):
                if word1[j] == word2[i]:
                    dp[j] = dpPrev[j+1]
                else:
                    dp[j] = min(dp[j+1], dpPrev[j], dpPrev[j+1]) + 1

        return dp[0]