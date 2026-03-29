import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # This is the same as heapify followed by a loop of size k
        # return heapq.nsmallest(k, points, key=lambda point: math.sqrt(point[0]**2 + point[1]**2))

        # "You may return the answer in any order"
        # This means we don't need them sorted, then we can quick select them, by using pivots and then filtering

        if len(points) <= k:
            return points

        def dist(point):
            # We do not need to sqrt since we only need to know who is bigger
            return point[0]**2 + point[1]**2

        def lt(point1, point2):
            return dist(point1) < dist(point2)

        def divide(arr):
            pivot = arr[0]
            L = []
            R = []
            M = []
            for i in range(len(arr)):
                if lt(arr[i], pivot):
                    L.append(arr[i])
                elif lt(pivot, arr[i]):
                    R.append(arr[i])
                else:
                    M.append(arr[i])

            return (L, M, R)
        res = []
        L = []
        M = []
        R = points
        while len(res) != k:
            print(res, L, R)
            if len(L) + len(res) <= k:
                res.extend(L)
                if len(res) + len(M) <= k:
                    res.extend(M)
                    L, M, R = divide(R)
                else: # if len(res) + len(M) > k:
                    res.extend(M[:k-len(res)])
            else: # if len(L) + len(res) > k:
                L, M, R = divide(L)

        return res