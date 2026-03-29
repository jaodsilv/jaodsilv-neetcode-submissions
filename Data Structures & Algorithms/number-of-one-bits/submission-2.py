# from collections import Counter
import math

class Solution:
    def hammingWeight(self, n: int) -> int:
        array = [1]*32
        for i in range(1, 32):
            array[i] = array[i-1] * 2
        count = 0
        array.reverse()
        for i in range(32):
            if n // array[i] > 0:
                count += 1
                n -= array[i]
        return count

        # return Counter(bin(n))['1'] Time and Space: O(log(n))
