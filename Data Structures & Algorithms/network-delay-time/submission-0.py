import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # We could do a dijkstra or a topological sorting
        # Let's do a BFS using a heap to keep the next item to be reached.
        if len(times) < n - 1:
            return -1


        # Let's build out adjacency list from that times list
        adj = [[] for _ in range(n + 1)]
        arrivalTime = [-1 for _ in range(n + 1)]
        for time in times:
            ui = time[0]
            vi = time[1]
            ti = time[2]
            adj[ui].append((ti, vi))
        
        visited = set()
        heap = [(0, k)]
        lastTime = 0
        while heap:
            node = heapq.heappop(heap)
            if node[1] in visited:
                continue
            lastTime = node[0]
            visited.add(node[1])

            for edge in adj[node[1]]:
                if edge[1] in visited:
                    continue
                heapq.heappush(heap, (lastTime + edge[0], edge[1]))
        return lastTime if len(visited) == n else -1

