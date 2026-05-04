class Solution:
    def reverse(self, x: int) -> int:
        MAXover10 = 214748364 # 214748364.7, if d > 7: 214748363, or when isNeg, and d > 6
        remainderChanger = 3
        negRemainderChanger = 2

        isNeg = x < 0
        if isNeg:
            x = -x
        
        res = 0
        while x:
            d = x%10
            if isNeg:
                # MAX = -MIN - 1 => -MIN = MAX+1
                # 214748364.7, if d > 7: 214748363, or when isNeg, and d > 8
                if d > 8:
                    if res > MAXover10-1:
                        return 0
                elif res > MAXover10:
                    return 0
            elif d > 7:
                if res > MAXover10-1:
                    return 0
            elif res > MAXover10:
                return 0

            res *= 10
            res += d
            x //= 10
        return -res if isNeg else res
