from collections import defaultdict
import heapq

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Let`s build the adjacency graph
        # BUT, for the neighbors, let`s use a list and sort it by the end to know which is the lexicographically smallest path
        adj = defaultdict(list)
        # airports = set()
        # O(tickets)
        for ticket in tickets:
            adj[ticket[0]].append(ticket[1])
        # sum(O(klogk)) = O(nlogn) where k is the number of tickets from that specific ariport
        # Sorting guarantees that during DFS, we visit the node with the smallest lexical order first
        for dests in adj.values():
            dests.sort()
        
        numTickets = len(tickets)
        # Now we do a dfs to find the smallest path that expends ALL tickets
        # Max depth = n => O(n) Space
        # Time: O(n)*??
        # It reaches maxDepth only once.
        # Worst case when ??
        def dfs(start, numTickets):
            if numTickets == 0:
                return [start]

            # O(n) * ??
            for i in range(len(adj[start])):
                dest = adj[start].pop(i)
                path = dfs(dest, numTickets - 1)
                if path is not None:
                    path.append(start)
                    return path
                adj[start].insert(i, dest)
            return None
        return dfs("JFK", numTickets)[::-1]
