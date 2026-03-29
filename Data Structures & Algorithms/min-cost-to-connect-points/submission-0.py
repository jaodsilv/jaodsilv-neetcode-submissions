import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def mdist(point1, point2):
            return abs(point1[0]-point2[0]) + abs(point1[1]-point2[1])
        
        if len(points) <= 1:
            return 0
        if len(points) == 2:
            return mdist(points[0], points[1])
        
        '''
        This a MST problem, where the edges are the paths and the nodes are the points
        Let's first build the graph
        '''

        adj = {}
        for i in range(len(points)):
            if i not in adj:
                adj[i] = {}
            for j in range(i + 1, len(points)):
                if j not in adj:
                    adj[j] = {}
                dist = mdist(points[i], points[j])
                adj[i][j] = dist
                adj[j][i] = dist

        # Now let's create the spanning the tree
        # Since it is an undirected graph it doesn't matter which node to start
        # Let's take the node 0 for instance.
        heap = [(0, 0)]
        cost = 0
        connected = set()
        while heap:
            point = heapq.heappop(heap)
            if point[1] in connected:
                continue
            cost += point[0]
            connected.add(point[1])
            for nei, dist in adj[point[1]].items():
                if nei not in connected:
                    heapq.heappush(heap, (dist, nei))
        return cost
