from collections import defaultdict
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Let's build the graph first
        graph = [[] for _ in range(n+1)]
        for srcc, dstt, price in flights:
            graph[srcc].append((price, dstt))
        # Now we do a modified dijkstra counting the stops
        # Note that we may add a flight more than once in the heap, but with different number of steps
        heap = [(price, 0, dstt) for price, dstt in graph[src]]
        heapq.heapify(heap)
        # k += 1 # To account the dst
        while heap:
            price, stops, stop = heapq.heappop(heap)
            if stops > k:
                continue
            if stop == dst:
                return price
            for legprice, dstt in graph[stop]:
                heapq.heappush(heap, (price+legprice, stops+1, dstt))
        return -1
