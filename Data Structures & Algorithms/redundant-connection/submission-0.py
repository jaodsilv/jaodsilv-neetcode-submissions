class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = set()
    def addNeighbor(self, neighbor):
        self.neighbors.add(neighbor)

class Graph:
    def __init__(self, edges):
        self.nodes = [None]*(len(edges) + 1)
        for edge in edges:
            if self.nodes[edge[0]] is None:
                self.nodes[edge[0]] = Node(edge[0])
            if self.nodes[edge[1]] is None:
                self.nodes[edge[1]] = Node(edge[1])
            node0 = self.nodes[edge[0]]
            node1 = self.nodes[edge[1]]
            node0.addNeighbor(node1)
            node1.addNeighbor(node0)

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Since it is guaranteed to have only one cycle, we need to first find that cycle
        graph = Graph(edges)

        # Now let's make this graph directions with a DFS
        # Since it is a DFS we guarantee the cycle is still there.
        def dfsCleaner(node, visited):
            if node in visited:
                return
            visited.add(node)
            for neighbor in node.neighbors.copy():
                if neighbor in node.neighbors:
                    neighbor.neighbors.discard(node)
                    if neighbor not in visited:
                        dfsCleaner(neighbor, visited)
                    

        # With no loss of generality, we can start by index 1
        dfsCleaner(graph.nodes[1], set())

        # Converting to list to guarantee the visiting order
        for i in range(1, len(graph.nodes)):
            node = graph.nodes[i]
            node.neighbors = list(node.neighbors)
        
        def dfsTravel(node, visited):
            if node in visited:
                return node
            visited.add(node)
            for n in node.neighbors:
                loopPoint = dfsTravel(n, visited)
                if loopPoint is not None:
                    return loopPoint
            return None

        visited = set()
        loopPoint = dfsTravel(graph.nodes[1], visited)
        print([x.val for x in visited], loopPoint.val)
        def dfsBuildLoop(node, loop, visited, init):
            if node == init:
                return
            if init is None:
                init = node

            print([x.val for x in node.neighbors], node.val)
            for n in node.neighbors[::-1]:
                if n in visited:
                    print(f'visited: {n.val}')
                    edge = [node.val, n.val]
                    loop.add((min(edge), max(edge)))
                    dfsBuildLoop(n, loop, visited, init)
                    return

        # To find the path of loop we need go through the last visited of neighbor of each node
        loop = set()
        dfsBuildLoop(loopPoint, loop, visited, None)

        print(loopPoint.val)
        print(loop)
        for edge in edges[::-1]:
            if (edge[0], edge[1]) in loop:
                return edge
