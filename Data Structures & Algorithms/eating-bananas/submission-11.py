class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        R = max(piles)
        L = max(1, sum(piles) // h)

        def compute(k: int):
            total = 0
            for p in piles:
                total += math.ceil(p / k)
            return total

        while L < R:
            k = (L + R) // 2
            vh = compute(k)
            print(L, k, R, vh)
            if vh <= h:
                R = k
            else:
                L = k+1
        return R