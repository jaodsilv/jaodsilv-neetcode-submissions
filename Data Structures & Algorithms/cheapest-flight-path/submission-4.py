import heapq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # We can BFS by lowest price distance
        fromToMap = defaultdict(list)
        for flight in flights:
            fromToMap[flight[0]].append((flight[2], flight[1]))
        if src not in fromToMap:
            return -1
        heap = [(0, src, -1)]
        visited = {}
        while heap:
            price, airport, stops = heapq.heappop(heap)
            # print(price, airport, stops)
            if airport == dst:
                return price
            visited[airport] = stops
            if stops < k:
                for localPrice, dest in fromToMap[airport]:
                    if visited.get(dest, k+1) > stops + 1:
                        heapq.heappush(heap, (price + localPrice, dest, stops + 1))
        return -1
