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

