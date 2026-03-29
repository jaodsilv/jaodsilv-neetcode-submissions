import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def solution1Heap():
            heapq.heapify_max(stones)
            while len(stones) > 1:
                top = heapq.heappop_max(stones)
                second = stones[0]
                if top == second:
                    heapq.heappop_max(stones)
                else:
                    heapq.heapreplace_max(stones, abs(top-second))
            return stones[0] if len(stones) == 1 else 0
        
        def solution2BucketSorting():
            lowest = min(stones)
            i = max(stones)
            buckets = [0]*(i + 1)

            for stone in stones:
                buckets[stone] += 1

            for j in range(1, len(buckets)):
                if buckets[i] <= 2:
                    continue
                if buckets[i] % 2 == 0:
                    buckets[i] = 2
                else:
                    buckets[i] = 1

            top = second = None
            while i > lowest or buckets[i] > 1 or (top and buckets[i]):
                print(i, buckets[i])
                while buckets[i]:
                    if top is None:
                        if buckets[i] == 2:
                            buckets[i] = 1
                        else:
                            top = i
                    else: # if second is None:
                        diff = abs(top-i)
                        buckets[diff] += 1
                        if diff > i:
                            buckets[i] -= 1
                            top = second = None
                            i = diff
                            continue

                        if diff:
                            lowest = min(diff, lowest)
                        
                        top = second = None
                    buckets[i] -= 1
                i -= 1
            # i == lowest
            if top is None:
                return i if buckets[i] else 0
            else:
                return top
        return solution2BucketSorting()