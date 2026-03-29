class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        def index(c):
            return ord(c)-ord('a')

        def char(i):
            return chr(i + ord('a'))

        count = [0]*26
        for i in range(len(s1)):  # O(len(s1))
            count[index(s1[i])] += 1
            count[index(s2[i])] -= 1

        maxValue = max(count) # O(26) = O(1)
        minValue = min(count) # O(26) = O(1)

        if minValue == maxValue:
            return True

        left = 0 # right = left + windowSize - 1
        for i in range(len(s1), len(s2)):
            cl = s2[i - len(s1)]
            cr = s2[i]
            print(cl, cr, minValue, maxValue, count)

            count[index(cl)] += 1
            count[index(cr)] -= 1

            if count[index(cr)] + 1 == minValue:
                minValue = count[index(cr)]
            elif count[index(cl)] - 1 == minValue:
                minValue = min(count)

            if count[index(cl)] - 1 == maxValue:
                maxValue = count[index(cl)]
            elif count[index(cr)] + 1 == maxValue:
                maxValue = max(count)
            
            if maxValue == minValue:
                return True
        return False
