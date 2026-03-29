import bisect
import heapq

class SegmentTree:
    def __init__(self, N):
        self.n = N
        self.tree = [10001] * (4 * N)
        self.lazy = [10001] * (4 * N)

    def propagate(self, treeidx, lo, hi):
        if self.lazy[treeidx] != 10001:
            self.tree[treeidx] = min(self.tree[treeidx], self.lazy[treeidx])
            if lo != hi:
                self.lazy[2*treeidx + 1] = min(self.lazy[2*treeidx + 1], self.lazy[treeidx])
                self.lazy[2*treeidx + 2] = min(self.lazy[2*treeidx + 2], self.lazy[treeidx])
            self.lazy[treeidx] = 10001
    
    def update(self, treeidx, lo, hi, left, right, val):
        self.propagate(treeidx, lo, hi)
        if lo > right or hi < left:
            return
        if lo >= left and hi <= right:
            self.lazy[treeidx] = min(self.lazy[treeidx], val)
            self.propagate(treeidx, lo, hi)
            return
        mid = (lo + hi) // 2
        self.update(2*treeidx + 1, lo, mid, left, right, val)
        self.update(2*treeidx + 2, mid + 1, hi, left, right, val)
        self.tree[treeidx] = min(self.tree[2*treeidx + 1], self.tree[2*treeidx + 2])
    
    def query(self, treeidx, lo, hi, idx):
        self.propagate(treeidx, lo, hi)
        if lo == hi:
            return self.tree[treeidx]
        mid = (lo + hi) // 2
        if idx <= mid:
            return self.query(2*treeidx + 1, lo, mid, idx)
        else:
            return self.query(2*treeidx + 2, mid+1, hi, idx)

    def updateRange(self, left, right, val):
        self.update(0, 0, self.n - 1, left, right, val)

    def queryPoint(self, idx):
        return self.query(0, 0, self.n - 1, idx)

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        def solutionMinSegmentTree():
            points = []
            for interval in intervals:
                points.append(interval[0])
                points.append(interval[1])
            for query in queries:
                points.append(query)

            points = sorted(set(points))
            compress = {points[i]: i for i in range(len(points))}

            segTree = SegmentTree(len(points))
            
            for interval in intervals:
                start = compress[interval[0]]
                end = compress[interval[1]]
                length = interval[1] - interval[0] + 1
                segTree.updateRange(start, end, length)
            ans = []
            for q in queries:
                idx = compress[q]

                res = segTree.queryPoint(idx)
                ans.append(res if res != 10001 else -1)
            return ans
        return solutionMinSegmentTree()
        