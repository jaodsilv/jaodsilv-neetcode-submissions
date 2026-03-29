from collections import defaultdict
import heapq

# Optimizing insertion and removal with a LL
class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Let`s build the adjacency graph
        # BUT, for the neighbors, let`s use a list and sort it by the end to know which is the lexicographically smallest path
        adj = defaultdict(list)
        adjLL = {}
        # airports = set()
        # O(tickets)
        for ticket in tickets:
            adj[ticket[0]].append(ticket[1])
        # sum(O(klogk)) = O(nlogn) where k is the number of tickets from that specific ariport
        # Sorting guarantees that during DFS, we visit the node with the smallest lexical order first
        for src, dests in adj.items():
            if len(dests) > 0:
                dests.sort()
                adjLL[src] = Node(dests[0])
                tail = adjLL[src]
                for i in range(1, len(dests)):
                    node = Node(dests[i])
                    tail.next = node
                    tail = node

        def popNext(parent):
            node = parent.next
            if node:
                parent.next = node.next
            return node
        def insertNext(parent, node):
            parent.next = node
        numTickets = len(tickets)
        # Now we do a dfs to find the smallest path that expends ALL tickets
        # Max depth = n => O(n) Space
        # Time: O(n)*??
        # It reaches maxDepth only once.
        # sum(O(k)) = O(E*V)
        # Worst case when the solution is always in the last edge of each node
        # When it is used, it is not seen again in deeper levels
        # When another one is used it can be used again once on each level
        # How many times we visit an edge?
        # i.e., it can be 'seen' once per visit per level. Therefore k² times, where k is the number of edges from that node
        # sum(O(k²))
        # We visit an edge only once per loop per node.
        # In this case we visit each edge at most node times, when it fails in the first, then in the second, in the third, and so on
        # A node being visited for the first time will have 
        def dfs(start, numTickets):
            if numTickets == 0:
                return [start]

            if len(adj[start]) == 0:
                return None

            # In a candidate path we only visit an edge once, thus O(k) with k being the edges departing from it
            node = adjLL[start]
            adjLL[start] = node.next
            path = dfs(node.val, numTickets - 1)

            if path is not None:
                path.append(start)
                return path

            adjLL[start] = node
            while node.next:
                parent = node
                node = popNext(node)
                path = dfs(node.val, numTickets - 1)
                if path is not None:
                    path.append(start)
                    return path
                insertNext(parent, node)
            return None

        return dfs("JFK", numTickets)[::-1]
