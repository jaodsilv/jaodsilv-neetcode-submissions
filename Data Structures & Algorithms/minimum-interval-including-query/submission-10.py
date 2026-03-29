from collections import deque

MAX_RANGE = 10001

class Node:
    def __init__(self, L: int, R: int, left = None, right = None, val = MAX_RANGE):
        self.L = L
        self.R = R
        self.left = left
        self.right = right
        self.val = val

    def addInterval(self, interval: List[int]) -> None:
        self._addInterval(interval[0], interval[1], interval[1] - interval[0] + 1)

    def _addInterval(self, L, R, length) -> int:
        if self is None or L > self.R or R < self.L:
            return MAX_RANGE

        if self.val <= length:
            return self.val

        if L <= self.L == self.R <= R:
            self.val = min(self.val, length)
            return self.val

        if self.val < MAX_RANGE:
            if L <= self.L and self.R <= R:
                self.val = length
                return self.val

            self.left.val = self.val
            self.right.val = self.val
        
        right = self.right.val
        left = self.left.val

        if L <= self.left.R:
            left = self.left._addInterval(L, R, length)
        if R >= self.right.L:
            right = self.right._addInterval(L, R, length)

        self.val = left if left == right else MAX_RANGE
        return self.val

    def query(self, query: int) -> int:
        if not self:
            return -1

        if self.L == self.R:
            return self.val if self.val != MAX_RANGE else -1

        if self.val != MAX_RANGE:
            return self.val
        
        if query <= self.left.R:
            return self.left.query(query)
        else:
            return self.right.query(query)

class SegmentTree:
    def __init__(self, items):
        self.root = None
        if items:
            self.root = self._insert(0, len(items) - 1, items)

    def _insert(self, L, R, items) -> Node | None:
        if L == R:
            return Node(items[L], items[L])
        mid = (L + R) // 2
        left = self._insert(L, mid, items)
        right = self._insert(mid + 1, R, items)
        node = Node(items[L], items[R], left, right)
        return node

    def addIntervals(self, intervals: List[List[int]]):
        if self.root:
            for interval in intervals:
                self.root.addInterval(interval)
                # print(f'Added interval {interval}. Result: {self}')

    def query(self, query: int) -> int:
        if self and self.root:
            return self.root.query(query)
        return -1

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        values = set()
        for L, R in intervals:
            values.add(L)
            values.add(R)
        for query in queries:
            values.add(query)
        tree = SegmentTree(sorted(values))
        tree.addIntervals(intervals)
        res = []
        for query in queries:
            res.append(tree.query(query))
        return res