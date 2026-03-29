import heapq

INFINITY = 4000001

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # We can do it building a MST
        # At each point we add we compute all points distances from it updating the minimum distance to reach each point

        # O(n²)
        dists = {i: INFINITY for i in range(1, len(points))}
        last = points[0]

        def dist(a, b):
            return abs(a[0]-b[0]) + abs(a[1]-b[1])

        total = 0
        while dists:
            closestPoint = -1
            minDist = INFINITY
            for k in dists.keys():
                dists[k] = min(dists[k], dist(last, points[k]))
                if dists[k] < minDist:
                    minDist = dists[k]
                    closestPoint = k
            total += minDist
            del dists[closestPoint]
            last = points[closestPoint]
        return total

