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
            buckets = [0]*101
            lowest = min(buckets)
            # highest = max(buckets)

            for stone in stones:
                buckets[stone] += 1

            i = 100
            top = second = None
            while i > lowest or buckets[i] > 1:
                while buckets[i]:
                    if top is None:
                        buckets[i] = buckets[i] % 2
                        if buckets[i]:
                            top = i
                    else: # if second is None:
                        second = i
                        buckets[abs(top-second)] += 1
                        lowest = min(abs(top-second), lowest) if abs(top-second) > 0 else lowest
                        top = second = None
                    buckets[i] -= 1
                i -= 1
            # i == lowest
            if top is None:
                return 0
            else:
                return top
        return solution1Heap()