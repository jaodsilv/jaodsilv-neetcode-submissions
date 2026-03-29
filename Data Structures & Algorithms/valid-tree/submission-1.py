class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # It is about detecting cycles, if we find 1 is good enough
        # First let's build a map of edges with the key being the nodes and the value being a pair of node and if it was visited

        visited = [False] * n
        edgesPerNode = []
        for i in range(n):
            edgesPerNode.append(set())

        for edge in edges:
            edgesPerNode[edge[0]].add(edge[1])
            edgesPerNode[edge[1]].add(edge[0])

        # If it is a tree we can start by ANY node actually, in particular we can start by node 0
        def visit(node):
            if visited[node]:
                return False
            visited[node] = True
            for i in edgesPerNode[node]:
                edgesPerNode[i].discard(node)
                if not visit(i):
                    return False
            edgesPerNode[node].clear()
            return True

        result = visit(0)

        # Now let's check if there is any non-connected node
        if result:
            for i in edgesPerNode:
                if len(i) > 0:
                    return False
            return True
        return False