from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        if len(s) == 1:
            return s if t == s else ""

        if len(t) == 1:
            return t if t in s else ""

        tCount = Counter(t)
        maxCount = tCount.most_common(1)[0]
        minLen = len(s) + 1
        minStr = ""
        i = 0

        # Find the first character of s that is in t
        while i < len(s):
            if s[i] in tCount:
                break
            else:
                i += 1
        
        tCount.subtract(s[i])
        j = i + 1

        while j < len(s) and s[j] not in tCount:
            j += 1
        if j < len(s):
            tCount.subtract(s[j])

        while j < len(s):
            print("i, j", i, j)

            print("tCount.most_common(1)[0][0]", tCount.most_common(1)[0][1])
            if tCount.most_common(1)[0][1] == 0:
                if j - i + 1 < minLen:
                    minLen = j - i + 1
                    minStr = s[i:(j+1)]
                tCount.update(s[i])
                i += 1
                while s[i] not in tCount:
                    i += 1
            else:
                j += 1
                while j < len(s) and s[j] not in tCount:
                    j += 1
                if j < len(s):
                    tCount.subtract(s[j])

        return minStr
