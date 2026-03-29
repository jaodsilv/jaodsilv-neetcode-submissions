class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #wordDict = set(wordDict)

        trues = [False]*(len(s) + 1)
        trues[0] = True
        for i in range(len(s)):
            if trues[i]:
                for word in wordDict: # Up to 20 words
                    if word == s[i:i + len(word)]:
                        trues[i + len(word)] = True
            
        return trues[-1]
        #def scan(remaining):
        #    if remaining in wordDict:
        #        return True
        #
        #    for i in range(len(remaining) - 1, 0, -1):
        #        if remaining[:i] in wordDict and scan(remaining[i:]):
        #            return True
        #    return False
        #return scan(s)