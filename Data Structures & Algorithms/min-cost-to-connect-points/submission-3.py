import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def mdist(i, j):
            return abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
        
        if len(points) <= 1:
            return 0
        if len(points) == 2:
            return mdist(0, 1)
        
        def prims1():
            '''
            This a MST problem, where the edges are the paths and the nodes are the points
            Since the graph is complete we can build the graph on the go, in a lazy manner to save memory
            Now let's create the spanning the tree
            Since it is an undirected graph it doesn't matter which node to start
            Let's take the node 0 for instance.
            '''
            pointsSet = set(range(len(points)))
            heap = [(0, 0)]
            cost = 0
            while heap:
                point = heapq.heappop(heap)
                if point[1] not in pointsSet:
                    continue
                cost += point[0]
                pointsSet.discard(point[1])
                for nei in pointsSet:
                    heapq.heappush(heap, (mdist(nei, point[1]), nei))
            return cost
        def prims2():
            dist = {i: float('infinity') for i in range(len(points))}
            # dist = [(float('infinity'), i) for i in range(len(points))]
            # heapq.heapify(dist)
            node = 0
            res = 0
            edges = 0
            del dist[node]
            while dist:
                mindist = float('infinity')
                minnode = -1
                for i in dist.keys():
                    cost = mdist(node, i)
                    dist[i] = min(dist[i], cost)
                    if dist[i] < mindist:
                        mindist = dist[i]
                        minnode = i
                node = minnode
                res += mindist
                del dist[node]
            return res

        return prims2()