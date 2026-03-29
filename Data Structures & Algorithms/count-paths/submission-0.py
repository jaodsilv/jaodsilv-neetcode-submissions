class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n == 1 or m == 1:
            return 1
        '''
        if m == 2 or n == 2:
            # Moves must contain 1 in shorter direction and x - 1 for x = max(m, n) the longer direction
            return max(m, n)
        if n == 3 and m >= 3: Or vice-versa
            moves must contain 2 down and 
        Generalizing
        We must have m-1 moves down and n-1 moves right
        So we do a permutation between them
        Total of m + n - 2 moves
        (m + n - 2)! / ((m - 1)!(n - 1)!)
        m = 3, n = 6 for example:
        (3 + 6 - 2)! / ((6 - 1)!(3 - 1)!) = 7! / (5!2!) = 7*6/2 = 7*3 = 21
        '''
        dividendFactor = m + n - 2
        divisorLeft = max(m, n) - 1
        divisorRight = min(m, n) - 1

        def comb(dividendFactor, divisorLeft, divisorRight):
            prod = 1
            for i in range(dividendFactor, divisorLeft, -1):
                prod *= i
            divisor = 1
            for i in range(2, divisorRight + 1):
                divisor *= i

            return prod // divisor
        return comb(dividendFactor, divisorLeft, divisorRight)
