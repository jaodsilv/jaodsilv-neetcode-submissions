from collections import defaultdict, deque
import heapq

class LLNode:
    def __init__(self, dest, left):
        self.left = left
        if left:
            left.right = self
        self.right = None
        self.dest = dest
    
    def autopop(self):
        if self.left:
            self.left.right = self.right
        if self.right:
            self.right.left = self.left

    def reinsert(self):
        if self.left:
            self.left.right = self
        if self.right:
            self.right.left = self

class TicketsLL:
    def __init__(self, tickets):
        self.tickets = {}
        for t in tickets:
            if t[0] not in self.tickets:
                root = LLNode(t[1], None)
                self.tickets[t[0]] = [root, root]
            else:
                node = LLNode(t[1], self.tickets[t[0]][1])
                self.tickets[t[0]][1] = node

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(key=lambda x: x[0] + x[1])

        def dfs(key: str, ll: TicketsLL, availableTickets: int):
            if availableTickets == 0:
                return [key]

            if key not in ll.tickets:
                return None

            root = ll.tickets[key][0]
            node = root
            availableTickets -= 1

            while node:
                node.autopop()
                if node == root:
                    ll.tickets[key][0] = root.right
                res = dfs(node.dest, ticketsLL, availableTickets)
                if res:
                    res.append(key)
                    return res
                if node == root:
                    ll.tickets[key][0] = root
                node.reinsert()
                node = node.right
            return None
            
        ticketsLL = TicketsLL(tickets)
        return dfs('JFK', ticketsLL, len(tickets))[::-1]
