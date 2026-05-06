class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # From any point, we can build a tree with the n-1 edges,
        # So, the n-th edge will close the tree.
        # Picking a random node
        # Let's make the graph an adjacency list graph
        n = len(edges)
        graph = [set() for _ in range(n+1)]
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])

        visited = set()
        def dfs(node):
            if node in visited:
                return node, {node}
            visited.add(node)
            while graph[node]:
                next = graph[node].pop()
                graph[next].discard(node)
                lastNode, res = dfs(next)
                if lastNode is not None:
                    if node == lastNode:
                        return None, res
                    else:
                        res.add(node)
                        return lastNode, res
                elif res is not None:
                    return None, res
                # next is not in the cycle
            # Node is not in the cycle
            return None, None

        # Let's first find the cycle
        _, nodes = dfs(1)
        for i in range(n-1, -1, -1):
            if edges[i][0] in nodes and edges[i][1] in nodes:
                return edges[i]
