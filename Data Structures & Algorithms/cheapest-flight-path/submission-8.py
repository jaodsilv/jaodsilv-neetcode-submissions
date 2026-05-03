from collections import defaultdict
from heapq import heappop, heappush
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Let's build the graph first
        graph = [[] for _ in range(n+1)]
        minPrices = [float('inf')]*n
        heap = []
        for srcc, dstt, price in flights:
            graph[srcc].append((price, dstt))
            if srcc == src:
                heappush(heap, (price, 0, dstt))

        # Now we do a modified dijkstra counting the stops
        # Note that we may add a flight more than once in the heap, but with different number of steps
        while heap:
            price, stops, stop = heappop(heap)
            if stop == dst:
                return price
            if stops < k:
                minPrices[stop] = price
                for legPrice, dstt in graph[stop]:
                    if legPrice + price < minPrices[dstt]:
                        heappush(heap, (price+legPrice, stops+1, dstt))
        return -1
