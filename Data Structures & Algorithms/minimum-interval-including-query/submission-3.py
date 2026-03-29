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

    # def __eq__(self, other):
    #     return self.diam == other.diam and self.end == other.end

    # def __gt__(self, other):
    #     return self.diam > other.diam or (self.diam == other.diam and self.end > other.end)

    # def __le__(self, other):
    #     return self.diam < other.diam or (self.diam == other.diam and self.end <= other.end)

    # def __ge__(self, other):
    #     return self.diam > other.diam or (self.diam == other.diam and self.end >= other.end)

    # def __ne__(self, other):
    #     return self.diam != other.diam or self.end != other.end

    def __str__(self):
        return f'[{self.start}, {self.end}]'

    def __repr__(self):
        return self.__str__()

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        def solutionGrouping():
            intervals = sorted([Interval(interval) for interval in intervals])

            # print(intervals)
            groupedIntervals = [(intervals[0].start, [intervals[0].end])]

            minStart = intervals[0].start
            maxEnd = intervals[0].end
            for i in range(1, len(intervals)):
                interval = intervals[i]
                if interval.start == groupedIntervals[-1][0]:
                    groupedIntervals[-1][1].append(interval.end)
                else:
                    groupedIntervals.append((interval.start, [interval.end]))
                maxEnd = max(maxEnd, interval.end)

            # print(groupedIntervals)
            # 1 more than the actual max, so it is an impossible number
            maxRange = maxEnd - minStart + 2
            sortedQueries = sorted(queries, reverse = True)
            # print(sortedQueries)
            findings = {}
            l = 0

            for query in sortedQueries:
                # print(f'query={query}')
                if query in findings:
                    continue
                if query > maxEnd or query < minStart:
                    findings[query] = -1
                    continue

                while groupedIntervals[-1][0] > query:
                    groupedIntervals.pop()

                # Even the minimum start may cover query,
                # however we can limit to the minimum possible length for a given i
                i = len(groupedIntervals) - 1
                minLength = maxRange

                while i >= 0 and query - groupedIntervals[i][0] + 1 < minLength:
                    if groupedIntervals[i][1][-1] < query:
                        # print(f'Skipping i={i}, start={groupedIntervals[i][0]}, ends={groupedIntervals[i][1]}')
                        i -= 1
                        continue

                    while len(groupedIntervals[i][1]) > 1 and groupedIntervals[i][1][-2] >= query:
                        groupedIntervals[i][1].pop()

                    # It is guaranteed that either groupedIntervals[i][1][-1] is the minimum possible intervals starting in start and covers query
                    minLength = min(minLength, groupedIntervals[i][1][-1] - groupedIntervals[i][0] + 1)
                    # print(f'i={i},start={groupedIntervals[i][0]},ends={groupedIntervals[i][1]},minLength={minLength}')
                    i -= 1

                findings[query] = -1 if minLength == maxRange else minLength

            res = []
            for query in queries:
                res.append(findings[query])

            return res

        def solutionBruteForce():
            res = []
            for query in queries:
                minLength = -1
                for interval in intervals:
                    if interval[0] <= query and interval[1] >= query:
                        tmp = interval[1] - interval[0] + 1
                        if minLength == -1:
                            minLength = tmp
                        else:
                            minLength = min(minLength, tmp)
                res.append(minLength)
            return res

        def solutionSweepLine():
            # Sorted Intervals by start decreasing
            intervals = sorted([Interval(interval) for interval in intervals], reverse=True)
            sortedQueries = sorted(queries, reverse = True)

            active = [] # Heap active intervals, keyed by diameter
            # print(intervals)

            findings = {}
            for query in queries:
                if intervals[-1].start > query:
                    finding[query] = -1
                while intervals[-1].start <= query:
                    interval = intervals.pop()
                    interval.byDiam = True
                    heapq.heappush(active, interval)
                while active[0].end < query:
                    heapq.heappop(active)
                if len(active) == 0:
                    findings[query] = -1
                else:
                    findings[query] = active[0].diam

            res = []
            for query in queries:
                res.append(findings[query])

            return res

        # return solutionGrouping()
        return solutionBruteForce()
        