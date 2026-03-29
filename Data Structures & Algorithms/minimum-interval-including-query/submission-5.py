import bisect
import heapq

class Interval:
    def __init__(self, interval):
        self.start = interval[0]
        self.end = interval[1]
        self.diam = self.end - self.start + 1
        self.byDiam = False

    def __lt__(self, other):
        if self.byDiam:
            return self.diam < other.diam or (self.diam == other.diam and self.end < other.end)
        else:
            return self.start < other.start or (self.start == other.start and self.end < other.end)

    def __str__(self):
        return f'[{self.start}, {self.end}]'

    def __repr__(self):
        return self.__str__()

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        def solutionSweepLine():
            # Sorted Intervals by start decreasing
            sortedIntervals = sorted([Interval(interval) for interval in intervals], reverse=True)
            sortedQueries = sorted(queries)

            print(sortedIntervals)
            print(sortedQueries)
            active = [] # Heap active intervals, keyed by diameter
            # print(intervals)

            findings = {}
            for query in sortedQueries:
                if len(sortedIntervals) == 0 or sortedIntervals[-1].start > query:
                    findings[query] = -1
                while sortedIntervals and sortedIntervals[-1].start <= query:
                    interval = sortedIntervals.pop()
                    interval.byDiam = True
                    heapq.heappush(active, interval)
                while active and active[0].end < query:
                    heapq.heappop(active)
                if len(active) == 0:
                    findings[query] = -1
                else:
                    findings[query] = active[0].diam

            res = []
            for query in queries:
                res.append(findings[query])

            return res

        return solutionSweepLine()
        