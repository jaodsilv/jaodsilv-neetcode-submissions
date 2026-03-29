import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Brute force
        L = 1
        R = max(piles) + 1
        while L < R:
            v = (L+R) // 2
            total = 0
            for p in piles:
                total += math.ceil(p / v)
            if total <= h:
                R = v
            else:
                L = v+1
        return L