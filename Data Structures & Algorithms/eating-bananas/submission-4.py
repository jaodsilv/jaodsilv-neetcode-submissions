from _bisect import bisect_left
import bisect
from collections import defaultdict
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        # For equidistributed piles, the result would be h = avg(piles)/speed=>h=(sum(piles)/len(piles))/speed => speed = sum(piles) / (h*len(piles))
        # buckets
        buckets = defaultdict(int)
        for p in piles:
            buckets[p] += 1
        values = sorted(buckets.keys())
        # | values that finish in 1 eating | 2* (values that finish in 2 eatings) | 3*...
        prefixSums = [buckets[values[0]]]
        for i in range(1, len(values)):
            prefixSums.append(prefixSums[-1] + buckets[values[i]])

        def total(s: int):
            return sum([buckets[v]*math.ceil(v / s) for v in values])
            # else:
            
            # j = s
            # i = max(0, bisect.bisect_right(values, s) - 1)
            # t = prefixSums[i]*(values[i]//s)
            # k = 2
            # while i < len(values):
            #     t += k*(prefixSums[i] - prefixSums[prev])
            #     prev = i
            #     j += v
            #     k += 1
            #     i = bisect.bisect_right(values, j, lo=prev+1) - 1
            # return t

        print(values)
        L, R = 1, values[-1]
        while L < R:
            v = (L + R) // 2
            t = total(v)
            print(v, t, L, R)
            if t <= h:
                R = v
            else:
                L = v+1
        print(L)
        return L

