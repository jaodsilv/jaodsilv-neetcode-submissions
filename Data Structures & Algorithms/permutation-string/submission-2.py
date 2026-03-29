class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s1):
            return False
        if len(s1) == 1:
            return s1 in s2
        origCounter = {} # Up to 26 elements
        for c in s1:
            if c in origCounter:
                origCounter[c] += 1
            else:
                origCounter[c] = 1
        
        # 2 pointers
        i = 0
        j = 0
        while j < len(s2):
            counter = origCounter.copy()
            total = len(s1)
            while j < len(s2) and s2[j] not in counter:
                j += 1
            i = j
            while j < len(s2) and j-i < len(s1) and s2[j] in counter:
                if counter[s2[j]] == 0:
                    while i < j and s2[i] != s2[j]:
                        counter[s2[i]] += 1
                        i += 1
                    if i < j:
                        counter[s2[i]] += 1
                        i += 1
                counter[s2[j]] -= 1
                j += 1

            print(counter)            
            if j-i == len(s1):
                return True
            
        return j-i == len(s1)
