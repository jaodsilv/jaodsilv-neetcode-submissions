import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Since the order is not relevant and there are repeated tasks
        # Let`s count each tasks
        print(Counter(tasks).values())
        maxheap = list(Counter(tasks).values())
        heapq.heapify_max(maxheap)
        blocked = {}

        n += 1
        count = 0
        print(maxheap)
        while maxheap or blocked:
            count += 1
            if count in blocked:
                heapq.heappush_max(maxheap, blocked[count])
                del blocked[count]
            if maxheap:
                v = heapq.heappop_max(maxheap)
                if v > 1:
                    blocked[count+n] = v - 1
            print(maxheap, blocked)

        return count

