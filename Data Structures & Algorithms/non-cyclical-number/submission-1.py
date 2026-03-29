class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True

        def sumOfSquares(num):
            res = 0
            while num:
                res += (num % 10)**2
                num //= 10
            return res

        slow = sumOfSquares(n)
        fast = sumOfSquares(slow)
        
        while slow != fast and fast > 1:
            slow = sumOfSquares(slow)
            fast = sumOfSquares(sumOfSquares(fast))
        return fast == 1
