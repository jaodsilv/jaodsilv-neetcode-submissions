class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        edgesMap = defaultdict(set)
        for edge in edges:
            edgesMap[edge[0]].add(edge[1])
            edgesMap[edge[1]].add(edge[0])
        nodes = set(range(n))
        def visit(node):
            for neighbor in edgesMap[node]:
                if neighbor in nodes:
                    edgesMap[neighbor].discard(node)
                    nodes.discard(neighbor)
                    visit(neighbor)
            del edgesMap[node]

        count = 0
        while nodes:
            count += 1
            visit(nodes.pop())

        return count