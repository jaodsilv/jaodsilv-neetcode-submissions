from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        maxCounter = 0
        maxLen = 0
        i, j = 0, 0
        while j < len(s):
            counter[s[j]] += 1
            maxCounter = max(counter[s[j]], maxCounter)
            j += 1
            while j - i - maxCounter > k:
                counter[s[i]] -= 1
                if maxCounter == counter[s[i]] + 1:
                    maxCounter = max(counter.values())
                i += 1
            maxLen = max(maxLen, j-i)
        return maxLen