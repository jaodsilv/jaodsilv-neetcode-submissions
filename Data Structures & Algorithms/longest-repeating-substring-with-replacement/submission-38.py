from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if k == 0:
            maxVal = 0
            curVal = 0
            last = None
            for c in s:
                if c == last:
                    curVal += 1
                else:
                    maxVal = max(maxVal, curVal)
                    last = c
                    curVal = 1
            return max(maxVal, curVal)

        # 2 pointers
        major = None
        cur = 0
        maxLen = 0
        diff = 0
        counter = defaultdict(int)
        counter[None] = 0
        m = len(s)
        L, R = 0, 0
        while R < m:
            if diff <= k: # I can still increase to the right
                c = s[R]
                counter[c] += 1
                maxLen = max(cur, maxLen)
                cur += 1
                if c != major:
                    if counter[c] > counter[major]:
                        major = c
                        # diff = R-L+1 - counter[c] # should not change diff
                    else:
                        diff += 1
                R += 1
            else: # if diff > k or R == m:
                c = s[L]
                cur -= 1
                maxLen = max(cur, maxLen)
                counter[c] -= 1
                L += 1
                if c == major: # it may need to be updated
                    for key, v in counter.items(): # Up to O(26)
                        if v > counter[major]:
                            major = key
                if c != major:
                    diff -= 1
            print(s[L:R], diff, maxLen, major)
        if diff <= k:
            maxLen = max(cur, maxLen)

        return maxLen if diff != k else max(R-L, maxLen)