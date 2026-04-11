import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Math
        counter = Counter(tasks)
        most_common = counter.most_common()
        maxf = most_common[0][1]
        idles = (maxf-1)*n
        maxCount = 1
        while maxCount < len(most_common) and maxf == most_common[maxCount][1]:
            maxCount += 1
        minRequiredTasks = (maxf - 1) * (n + 1) + maxCount
        return max(len(tasks), minRequiredTasks)

        # Greedy
        counter = Counter(tasks)
        most_common = counter.most_common()
        maxf = most_common[0][1]
        idles = (maxf-1)*n

        for t, c in most_common[1:]:
            idles -= min(c, maxf-1)
        return len(tasks) + max(idles, 0)

        # maxheap
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

