class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        for a, b in zip(word1, word2):
            res.append(a + b)
        cut = min(len(word1), len(word2))
        res.append(word1[cut:])
        res.append(word2[cut:])
        return ''.join(res)