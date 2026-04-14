class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x, y = point
            heapq.heappush(heap, (math.sqrt(x**2 + y**2),point))
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans