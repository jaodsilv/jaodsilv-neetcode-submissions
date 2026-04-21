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
                # print(f'head: {i}')
                return ({i}, True)
            visited.add(i)
            if len(graph[i]) == 0:
                # print(f'{i} has no other edges')
                return None, None
            for nei in graph[i]:
                graph[nei].discard(i)
                cycle, add = dfs(nei, visited)
                if cycle is not None:
                    # print(f'Cycle detected We are in i: {i}, nei: {nei}')
                    if add and nei in cycle and i not in cycle:
                        # print(f'Cycle detected We are in {i}')
                        cycle.add(i)
                    else:
                        add = False
                    return (cycle, add)
            # print(f'Cycle not reacheable from {i}')
            return None, None
        cycle, _ = dfs(1, set())
        # print(cycle)
        for edge in edges[::-1]:
            if edge[0] in cycle and edge[1] in cycle:
                return edge
        # Now that we have the cycle we find the last edge from the edges