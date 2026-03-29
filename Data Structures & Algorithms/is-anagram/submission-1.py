from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = Counter(s)
        for c in t:
            if c not in s:
                return False
            s[c] -= 1
            if s[c] == 0:
                del s[c]
        return len(s) == 0