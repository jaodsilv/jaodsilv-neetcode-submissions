from collections import deque
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        # Radix sort
        ## We have the range from -50_000 to 50_000, therefore we should use a base that makes sense for that for the buckets
        ## Powers of 2 would be a good start
        def merge(arr1: deque[int], arr2: deque[int]) -> deque[int]:
            '''
            merge the ranges from l to m and from m+1 to r, inclusive
            '''
            res = deque()
            while arr1 and arr2:
                if arr1[0] < arr2[0]:
                    res.append(arr1.popleft())
                else:
                    res.append(arr2.popleft())
            if arr1:
                res.extend(arr1)
            else:
                res.extend(arr2)
            return res

        def radix(arr: deque[int], base: int) -> deque[int]:
            if len(arr) <= 1:
                return arr
            buckets = deque([deque() for _ in range(base)])
            maxVal = 0
            for n in arr:
                buckets[abs(n) % base].append(n)
                maxVal = max(maxVal, abs(n))
            if maxVal < base:
                # This means this group is totally sorted already
                res = deque()
                for bucket in buckets:
                    for j in bucket:
                        if j < 0:
                            res.appendleft(j)
                        else:
                            res.append(j)
                return res
            nextBase = base << 1
            for i in range(base):
                buckets[i] = radix(buckets[i], nextBase)
            while len(buckets) > 1:
                b1 = deque()
                while buckets and not b1:
                    b1 = buckets.popleft()
                b2 = deque()
                while buckets and not b2:
                    b2 = buckets.popleft()
                if not b2:
                    return b1
                buckets.append(merge(b1, b2))
            return buckets[0]
        return list(radix(deque(nums), 2))