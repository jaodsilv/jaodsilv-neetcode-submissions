import math
class Solution:
    def reverse(self, x: int) -> int:
        if x > -10 and x < 10:
            return x

        MAX_INT = 2147483647
        # So the limits to test are:
        # 2143847412, meaning if the number is greater than this
        # We test first for the number of digits
        # MIN_INT = -2147483648

        digits = math.floor(math.log10(abs(x))) + 1
        isNegative = x < 0
        x = abs(x)
        tens = 10 ** (digits - 1)
        print(digits)
        print(tens)
        total = 0

        # Test last digit to avoid using a number bigger than MAX_INT
        if digits == 10 and x % 10 > 2:
            return 0

        for i in range(digits, 0, -1):
            toSum = (x % 10) * (tens)
            if total > MAX_INT - toSum:
                return 0
            if isNegative and total > MAX_INT - toSum + 1:
                return 0

            x //= 10
            tens //= 10
            total += toSum
        return -total if isNegative else total
    
