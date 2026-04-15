import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k >= len(points):
            return points
        # def dist_center(x, y) -> float:
            # return math.sqrt(
            # return x**2 + y**2
                # )
    
        # def pivot(dists, L, R) -> tuple[int, float]:
            # return random.choice(dists[L:R])
            # return 
            # d0 = dists[0]
            # d1 = dists[len(dists) // 2]
            # d2 = dists[-1]
            # return (d0+d1+d2) / 3

        # First let's compute once all the distances
        dists = []
        for i in range(len(points)):
            dists.append(points[i][0]**2 + points[i][1]**2)

        # Now let's quick-search style divide the array into the k closest vs the n-k farthest
        L, R = 0, len(points)
        while L != k and R != k:
            # if L >= R:
            #     return 0
            p = (dists[L] + dists[R-1]) // 2
            i = L
            prevL, prevR = L, R
            while i < R:
                if dists[i] < p:
                    dists[i], dists[L] = dists[L], dists[i]
                    points[i], points[L] = points[L], points[i]
                    L += 1
                    i += 1
                elif dists[i] > p:
                    R -= 1
                    dists[i], dists[R] = dists[R], dists[i]
                    points[i], points[R] = points[R], points[i]
                else:
                    i += 1
            # Dists[:L] are all less than p
            # Dists[L:R] have all the same distance = p
            # Dists[R:] are all greater than p
            if R < k:
                L = R
                R = prevR
            elif R == k:
                return points[:R]
            elif L < k: # R > k
                # process from L to R
                pass
            elif L == k:
                return points[:L]
            else: # L > k
                R = L
                L = prevL
            # print(L, R, k, prevL, prevR, p)

        return points[:L]