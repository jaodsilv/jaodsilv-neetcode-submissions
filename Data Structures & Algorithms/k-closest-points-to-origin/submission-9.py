import math
import random

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k >= len(points):
            return points
        def dist_center(x, y) -> float:
            return math.sqrt(x*x + y*y)
    
        def pivot(dists) -> float:
            return random.choice(dists)
            # return (dists[0] + dists[-1]) // 2
            # d0 = dists[0]
            # d1 = dists[len(dists) // 2]
            # d2 = dists[-1]
            # return (d0+d1+d2) / 3

        # First let's compute once all the distances
        dists = []
        for i in range(len(points)):
            dists.append(dist_center(points[i][0], points[i][1]))
        # Now let's quick-search style divide the array into the k closest vs the n-k farthest

        res = []
        while len(res) < k:
            closestP = []
            closestD = []
            farthestD = []
            farthestP = []
            exactP = []
            exactD = []
            p = pivot(dists)
            for i in range(len(dists)):
                if dists[i] > p:
                    farthestP.append(points[i])
                    farthestD.append(dists[i])
                elif dists[i] < p:
                    closestP.append(points[i])
                    closestD.append(dists[i])
                else:
                    exactP.append(points[i])
                    exactD.append(dists[i])
            if len(res) + len(closestP) <= k:
                res.extend(closestP)
                if len(res) + len(exactP) <= k:
                    dists = farthestD
                    points = farthestP
                    res.extend(exactP)
                else:
                    dists = exactD
                    points = exactP
            else:
                dists = closestD
                points = closestP
            # print(res, points)

        return res