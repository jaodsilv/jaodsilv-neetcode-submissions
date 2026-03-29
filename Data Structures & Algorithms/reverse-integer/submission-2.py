import math
class Solution:
    def reverse(self, x: int) -> int:
        if x > -10 and x < 10:
            return x

        MAX_INT = 2147483647
        MIN_INT = -2147483648
        if x > MAX_INT or x < MIN_INT:
            return 0

        isNegative = x < 0
        asStr = str(abs(x))
        if len(asStr) == 10 and int(asStr[-1]) > 2:
            return 0
        total = 0
        tens = 1
        for d in asStr:
            d = int(d) * tens
            if total > MAX_INT - d + 1 or (not isNegative and total == MAX_INT - d + 1):
                return 0
            tens *= 10
            total += d
        return -total if isNegative else total

