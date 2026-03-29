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
        clone = Node(node.val)
        builtNodes = {clone.val: clone}
        def dfs(node, copy):
            for nei in node.neighbors:
                neiClone = None
                if nei.val in builtNodes:
                    neiClone = builtNodes[nei.val]
                else:
                    neiClone = Node(nei.val)
                    builtNodes[nei.val] = neiClone
                    dfs(nei, neiClone)
                copy.neighbors.append(neiClone)
        dfs(node, clone)
        return clone
                    
