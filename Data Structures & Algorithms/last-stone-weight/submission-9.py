import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # max len(stones) is 20, sorting it or keeping a heap would give us O(20log20) < O(100)
        heap = [0]
        for stone in stones:
            heapq.heappush_max(heap, stone)
        i = heapq.heappop_max(heap)
        curr = 0
        while i:
            print(i, heap)
            if curr == 0:
                curr = i
            else:
                heapq.heappush_max(heap, curr-i)
                curr = 0
            i = heapq.heappop_max(heap)
        return curr