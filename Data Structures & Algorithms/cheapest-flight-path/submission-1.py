import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # We can BFS by lowest price distance
        fromToMap = {}
        toFromMap = {}
        for flight in flights:
            if flight[0] not in fromToMap:
                fromToMap[flight[0]] = [(flight[2], flight[1])]
            else:
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
