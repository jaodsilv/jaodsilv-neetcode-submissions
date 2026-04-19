class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        f = 0

        l1, l2 = len(word1), len(word2)
        m = min(l1, l2)-1
        ans = []
        while f <= m:
            ans.append(word1[f])
            ans.append(word2[f])
            f += 1
        if l1 > l2:
            ans.append(word1[f:])
        elif l2 > l1:
            ans.append(word2[f:])
        
        return ''.join(ans)