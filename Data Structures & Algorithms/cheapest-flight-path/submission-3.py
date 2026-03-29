import heapq
from collections import defaultdict, deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        def solutionHeap():
            # We can BFS by lowest price distance
            fromToMap = defaultdict(list)
            for flight in flights:
                fromToMap[flight[0]].append((flight[2], flight[1]))
            if src not in fromToMap:
                return -1
            heap = [(x[0], x[1], 0) for x in fromToMap[src]]
            heapq.heapify(heap)
            visited = {src}
            while heap:
                price, airport, stops = heapq.heappop(heap)
                print(price, airport, stops)
                if airport == dst:
                    return price
                visited.add(airport)
                if stops < k and airport in fromToMap:
                    destinations = fromToMap[airport]
                    for localPrice, destination in destinations:
                        if destination not in visited:
                            heapq.heappush(heap, (price + localPrice, destination, stops + 1))
            return -1
        def solutionBFS():
            # We can BFS to calculate ALL the distances from src
            # First let's build the adjacency list graph
            routes = defaultdict(list)
            prices = [0]*n
            for flight in flights:
                routes[flight[0]].append(flight)
            if src not in routes:
                return -1
            queue = deque(routes[src])
            for _ in range(k + 1):
                tmpPrices = prices.copy()
                for i in range(len(queue)):
                    route = queue.popleft()
                    if route[1] == src:
                        continue
                    tmpPrice = prices[route[0]] + route[2]
                    if tmpPrices[route[1]] == 0:
                        tmpPrices[route[1]] = tmpPrice
                    else:
                        tmpPrices[route[1]] = min(tmpPrices[route[1]], tmpPrice)
                    queue.extend(routes[route[1]])
                prices = tmpPrices
            return prices[dst] if prices[dst] > 0 else -1
        return solutionBFS()
