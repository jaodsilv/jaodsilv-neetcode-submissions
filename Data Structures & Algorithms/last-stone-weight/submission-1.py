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
        return solution1Heap()