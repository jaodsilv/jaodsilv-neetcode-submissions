from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = defaultdict(int) # O(26)
        for c in t:
            counter[c] += 1
            
        gt0 = len(counter)
        minLen = len(s) + 1
        minLenL = -1
        minLenR = len(s) + 1
        R = 0
        while R < len(s) and s[R] not in counter:
            R += 1
        L = R

        print(0, L, R, minLenL, minLenR, gt0, s[minLenL:minLenR])
        while R < len(s):
            while R < len(s) and gt0 > 0:
                if s[R] in counter:
                    counter[s[R]] -= 1
                    if counter[s[R]] == 0:
                        gt0 -= 1
                R += 1
            print(1, L, R, minLenL, minLenR, gt0, s[minLenL:minLenR])
            while gt0 == 0:
                if s[L] in counter:
                    counter[s[L]] += 1
                    if counter[s[L]] == 1:
                        gt0 += 1
                        if R-L < minLen:
                            minLen = R-L
                            minLenL = L
                            minLenR = R
                L += 1
            print(2, L, R, minLenL, minLenR, gt0, s[minLenL:minLenR])

        if gt0 == 0 and R-L < minLen:
            minLenL, minLenR = L, R
            print(3, L, R, minLenL, minLenR, gt0, s[minLenL:minLenR])
        if minLenR == len(s) + 1:
            return ""
        else:
            return s[minLenL:minLenR]
