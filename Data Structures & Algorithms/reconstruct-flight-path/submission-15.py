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
        tickets.sort(key=lambda x: x[0] + x[1], reverse=True)
        trip = {}
        for t in tickets:
            if t[0] not in trip:
                trip[t[0]] = [t[1]]
            else:
                trip[t[0]].append(t[1])

        def fly(orig: str, trip: dict) -> list[str]:
            if orig not in trip:
                return [orig]
            res = []
            dests = trip[orig]
            while dests:
                dest = dests.pop()
                res.extend(fly(dest, trip))
            res.append(orig)
            return res
            
        return fly('JFK', trip)[::-1]
