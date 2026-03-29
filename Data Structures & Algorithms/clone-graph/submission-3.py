"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import defaultdict

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        nodes = defaultdict(list)

        def dfs(node):
            if node.val in nodes:
                return nodes[node.val]

            copy = Node(node.val)
            nodes[node.val] = copy
            for n in node.neighbors:
                neighbor = dfs(n)
                copy.neighbors.append(neighbor)
            return copy

        return dfs(node)


        