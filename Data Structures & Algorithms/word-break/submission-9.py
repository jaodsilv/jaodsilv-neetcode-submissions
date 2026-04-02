class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        This seems a case for DP
           n e e t c o d e
             e e
        '''

        DP = [True] + [False]*len(s)
        words = set(wordDict)
        # O(n²) Solution
        for i in range(len(s)):
            if not DP[i]:
                continue
            for j in range(i+1, len(s)+1):
                if s[i:j] in words:
                    DP[j] = True
        return DP[-1]