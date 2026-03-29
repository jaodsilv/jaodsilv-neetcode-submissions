class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if x == 0:
            return 0

        if n < 0:
            x = 1 / x
            n = -n

        memo = {0: 1, 1: x}
        def _pow(x, n):
            if n in memo:
                return memo[n]
            res = _pow(x, n // 2) * _pow(x, n // 2)
            if n % 2 == 1:
                res *= x
            memo[n] = res
            return res

        return _pow(x, n)
        '''
        pow(2, 25) => _pow(2, 12)*_pow(2, 12)*2
        _pow(2, 12) => _pow(2, 6)*_pow(2, 6)

        '''