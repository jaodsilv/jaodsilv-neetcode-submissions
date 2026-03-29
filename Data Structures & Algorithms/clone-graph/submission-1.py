"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        neighbors = []
        for i in range(101):
            neighbors.append(set())
        visited = set()

        def getNeighbors(node):
            if node.val in visited:
                return
            visited.add(node.val)
            for neighbor in node.neighbors:
                neighbors[node.val].add(neighbor.val)
                getNeighbors(neighbor)
        getNeighbors(node)

        count = len(visited)

        newNodes = [None] * (count + 1)

        for i in range(1, count + 1):
            newNodes[i] = Node(i)

        for i in range(1, count + 1):
            for neighbor in neighbors[i]:
                newNodes[i].neighbors.append(newNodes[neighbor])
        return newNodes[node.val]