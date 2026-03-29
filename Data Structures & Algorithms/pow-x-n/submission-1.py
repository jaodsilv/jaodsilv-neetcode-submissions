class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if x == 0:
            return 0

        if n < 0:
            x = 1 / x
            n = -n

        def _pow(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            res = _pow(x, n // 2) * _pow(x, n // 2)
            if n % 2 == 1:
                res *= x
            return res

        return _pow(x, n)