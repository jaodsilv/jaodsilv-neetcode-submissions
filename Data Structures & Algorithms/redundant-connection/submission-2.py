from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Let's build the adjacency graph first
        graph = defaultdict(set)
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])
        # We have now to find the cycle
        # Let's first find the cycle
        # To start, let's take the last edge 0th node withn no loss of generality
        
        def dfs(i, visited):
            if i in visited:
                return [i]
            visited.add(i)
            if len(graph[i]) == 0:
                return None
            for nei in graph[i]:
                graph[nei].discard(i)
                ret = dfs(nei, visited)
                if ret is not None:
                    if nei == ret[-1] and (len(ret) == 1 or nei != ret[0]):
                        ret.append(i)
                    return ret
            return None
        cycle = dfs(1, set())
        cycleEdges = {(cycle[i],cycle[i+1]) for i in range(len(cycle) - 1)} | {(cycle[i+1],cycle[i]) for i in range(len(cycle) - 1)}
        
        for edge in edges[::-1]:
            if tuple(edge) in cycleEdges:
                return edge
        # Now that we have the cycle we find the last edge from the edges