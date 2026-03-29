import bisect
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        
        def test(v):
            t = 0
            for p in piles:
                t += math.ceil(p/v)
            return t

        L, R = 1, max(piles)
        while L < R:
            v = (L + R) // 2
            t = test(v)
            print(L, R, v, t)
            if t <= h:
                R = v
            else:
                L = v+1
        print(L)
        return L

