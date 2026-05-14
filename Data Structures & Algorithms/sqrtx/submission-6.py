class Solution:
    def mySqrt(self, x: int) -> int:
        # First candidade = x // 2
        L, R = 0, x
        cand = x // 2
        # (cand+1) * (cand+1) = cand*cand + 2*cand + 1 > x
        # cand*cand <= x < cand*cand + 2*cand + 1
        while True: #not (p <= x < p + 2*cand + 1):
            p = cand*cand
            if p <= x < p + 2*cand + 1:
                return cand
            elif p > x:
                R = cand-1
                cand = (L + R) // 2
            elif x >= p + 2*cand + 1:
                L = cand+1
                cand = (L + R) // 2
            
        return cand
