from collections import defaultdict
import heapq

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Let`s build the adjacency graph
        # BUT, for the neighbors, let`s use a list and sort it by the end to know which is the lexicographically smallest path
        adj = defaultdict(list)
        # airports = set()
        for ticket in tickets:
            adj[ticket[0]].append([ticket[1], False])
        for dests in adj.values():
            dests.sort(key=lambda x: x[0])
        
        numTickets = len(tickets)
        # Now we do a dfs to find the smallest path that expends ALL tickets
        def dfs(start, numTickets):
            if numTickets == 0:
                return [start]
            for i in range(len(adj[start])):
                dest = adj[start][i]
                if dest[1]:
                    continue
                dest[1] = True
                path = dfs(dest[0], numTickets - 1)
                if path is not None:
                    path.append(start)
                    return path
                else:
                    dest[1] = False

            return None
        return dfs("JFK", numTickets)[::-1]
