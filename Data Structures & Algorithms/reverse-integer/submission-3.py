import math
class Solution:
    def reverse(self, x: int) -> int:
        if x > -10 and x < 10:
            return x

        MAX_INT = 2147483647
        MIN_INT = -2147483648
        if x > MAX_INT or x < MIN_INT:
            return 0
        # So the limits to test are:
        # 2143847412, meaning if the number is greater than this
        # We test first for the number of digits

        # Since we are bount to MAX_INT, digits <= 10
        isPositive = x > 0
        x = abs(x)
        total = 0

        # O(digits) = O(10) = O(1)
        while x > 0:
            lastDigit = x % 10
            if total > (MAX_INT - lastDigit + 1) / 10:
                return 0
            if isPositive and total > (MAX_INT - lastDigit) / 10:
                return 0

            x //= 10
            total = total*10 + lastDigit
        return total if isPositive else -total
    
