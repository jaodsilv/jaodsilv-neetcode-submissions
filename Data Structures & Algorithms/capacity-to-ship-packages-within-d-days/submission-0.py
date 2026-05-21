from bisect import bisect_right
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        maxW = weights[0]

        if len(weights) == 1:
            return maxW

        prefix = [0]
        for w in weights:
            prefix.append(w + prefix[-1])
            maxW = max(maxW, w)

        if days >= len(weights):
            return maxW

        if days == 1:
            return prefix[-1]

        # print('test')
        # return 0
        # dp = [0]*(days+1)
        def total_days(cap) -> int:
            res = 0
            index = 0
            v = 0
            # count = 5
            while index < len(prefix)-1: # and count:
                # print('index', index, v, cap+v)
                # count -= 1
                res += 1
                index = bisect_right(prefix, cap+v, lo=index)-1
                v = prefix[index]
            return res

        # Min possible
        L = max(maxW, prefix[-1] // days)
        # Worst case possible, we fit everything in a single run
        R = prefix[-1]
        # print(L, R)
        lastTested = 0
        # count = 5
        while L < R: # and count:
            # count -= 1
            capacity = (L+R) // 2
            if capacity == lastTested:
                return capacity
            lastTested = capacity
            res = total_days(capacity)
            if res > days:
                L = capacity + 1
            else:
                R = capacity
            # print(res, L, R)
        return L