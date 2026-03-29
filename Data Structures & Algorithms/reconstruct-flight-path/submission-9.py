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
        adj = defaultdict(list)
        adjLL = {}

        # O(tickets)
        for ticket in tickets:
            adj[ticket[0]].append(ticket[1])

        # Sorting guarantees that during DFS, we visit the node with the smallest lexical order first
        # Sorting all is sum(O(klogk)) = O(nlogn) where k is the number of tickets from that specific ariport
        # Creating the LLs is sum(O(k)) = O(n)
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

        def dfs(start, numTickets):
            if numTickets == 0:
                return [start]

            if len(adj[start]) == 0:
                return None

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
