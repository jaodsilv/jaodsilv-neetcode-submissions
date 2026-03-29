class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        # Dummy solultion: Do a binary search on the closes value
        L = 0 # 0
        R = x // 2 # 2
        while R > L + 1: # 2 > 0, 
            M = (L + R) // 2 # M = 1
            s = M*M # s = 4, s
            if s == x:
                return M
            if s > x:
                # M is not an option
                R = M - 1
            else: # 4 < 9
                # M is still a possibility
                L = M # L = 2
        if R*R > x:
            return L
        return R
        