import heapq
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = dict(Counter(t))
        # Strip s for characters not present in t in the sides of the str
        for i in range(len(s)):
            c = s[i]
            if c in counter:
                if i > 0:
                    s = s[i:]
                break
        for i in range(len(s), 0, -1): # item 0 surely is in t
            c = s[i-1]
            if c in counter:
                if i < len(s):
                    s = s[:i]
                break

        if len(t) > len(s):
            return ""
        # if len(t) == len(s):
        #     return t if t == s else ""
        if t in s:
            return t
        # Using a heap so we can keep track of the most common characters

        # This functions is O(26)=O(1) time
        def getMostCommon():
            val = 0
            res = set()
            for c, v in counter.items():
                if v == val:
                    res.add(c)
                elif v > val:
                    res = {c}
                    val = v
            return val, res
        # heap = [[count, count, char] for char, count in counter.items()]
        # heapq.heapify_max(heap)

        # counter = {item[2]: item for item in heap}

        minLen = len(s)+1
        minL = 0
        minR = len(s)

        i, j = 0, 0
        print(counter)
        while j < len(s):
            count, mostCommon = getMostCommon()
            while j < len(s) and count > 0:
                c = s[j]
                if c not in counter:
                    j += 1
                    continue
                counter[c] -= 1
                if c in mostCommon:
                    mostCommon.discard(c)
                    if not mostCommon:
                        count, mostCommon = getMostCommon()
                j += 1
            print(counter, s[i:j], s[minL:minR])
            while i < j and (count == 0 or s[i] not in counter):
                # Update minLen
                if count == 0 and j-i < minLen:
                    minL = i
                    minR = j
                    minLen = j-i
                c = s[i]
                i += 1
                if c not in counter:
                    continue
                counter[c] += 1
                if counter[c] > 0:
                    mostCommon = {c}
                    count = 1
            print(counter, s[i:j], s[minL:minR])
        # Update minLen
        if count == 0 and j-i < minLen:
            minLen = j-i
            minL = i
            minR = j

        return "" if minLen == len(s) + 1 else s[minL:minR]