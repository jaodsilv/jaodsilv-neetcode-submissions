from collections import deque
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        positives = []
        negatives = []
        for n in nums:
            if n < 0:
                negatives.append(n)
            else:
                positives.append(n)

        # primeRadix sort
        ## We have the range from -50_000 to 50_000, therefore we should use a base that makes sense for that for the buckets
        ## Powers of 4 would be a good start. Since the range of values is -50k to 50k, we will have up to 8 levels in the worst case
        def merge(arr1: list[int], arr2: list[int]) -> list[int]:
            '''
            merge the ranges from l to m and from m+1 to r, inclusive
            '''
            res = []
            i, j = 0, 0
            while i < len(arr1) and j < len(arr2):
                if arr1[i] < arr2[j]:
                    res.append(arr1[i])
                    i += 1
                else:
                    res.append(arr2[j])
                    j += 1
            return res + arr1[i:] + arr2[j:]

        primes = [2,3,5,7,11,13,17]
        def primeRadix(arr: list[int], primeIndex: int) -> list[int]:
            if len(arr) <= 1 or max(arr) == min(arr):
                return arr
            base = primes[primeIndex]
            buckets = [[] for _ in range(base)]
            for n in arr:
                buckets[abs(n) % base].append(n)
            if base > 11:
                print(f'buckets: {primes[primeIndex]}')
            j = 0
            for i in range(base):
                if buckets[i]:
                    buckets[j] = primeRadix(buckets[i], primeIndex+1)
                    j+=1
            buckets = buckets[:j]
            # print(f'buckets: {primes[primeIndex]} => {buckets}')

            while len(buckets) > 1:
                b1 = None
                b2 = None
                j = 0
                for i in range(len(buckets)):
                    if not b1:
                        b1 = buckets[i]
                    elif not b2:
                        b2 = buckets[i]
                    else:
                        buckets[j] = merge(b1, b2)
                        b1 = buckets[i]
                        b2 = None
                        j += 1
                if b1:
                    if b2:
                        buckets[j] = merge(b1, b2)
                    else:
                        buckets[j] = b1
                    j += 1
                buckets = buckets[:j]
                # print(f'buckets: {primes[primeIndex]} => {buckets}')
            return buckets[0]

        res = primeRadix(negatives, 0) + primeRadix(positives, 0)
        if 50 < len(nums) < 100:
            return
        return res
        
