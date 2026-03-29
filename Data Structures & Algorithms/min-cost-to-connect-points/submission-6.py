import heapq

MAX_DIST = 4000001

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0

        def dist(a, b):
            return abs(a[0]-b[0]) + abs(a[1]-b[1])
        # Create Nodes
        nodes = [(p[0], p[1]) for p in points]
        
        # Process Nodes one by one, finding the minimum Distance Node
        total = 0
        notConnected = set(range(1, len(nodes)))
        dists = [MAX_DIST]*len(nodes)
        dists[0] = 0
        nextNode = 0
        edges = 0
        while edges < len(nodes) - 1:
            node = nodes[nextNode]
            nextNode = None
            minCost = MAX_DIST
            for j in notConnected:
                m = nodes[j]
                dists[j] = min(dists[j], dist(node, m))
                if minCost > dists[j]:
                    minCost = dists[j]
                    nextNode = j
            edges += 1
            total += minCost
            notConnected.discard(nextNode)
        return total



