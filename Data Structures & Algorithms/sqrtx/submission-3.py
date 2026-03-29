class Solution:
    def mySqrt(self, x: int) -> int:
        # Newton's method
        r = x
        while r * r > x:
            r = (r + x / r) // 2
        return math.floor(r)
        