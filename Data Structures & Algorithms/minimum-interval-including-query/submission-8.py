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
        if self is None:
            return MAX_RANGE
        if L > self.R or R < self.L:
            return MAX_RANGE

        if self.val < length:
            return self.val

        if L <= self.L == self.R <= R:
            self.val = min(self.val, length)
            return self.val

        isTotalMatch = L <= self.L and R >= self.R

        mid = (self.L + self.R) // 2
        if self.left:
            mid = self.left.R
        elif self.right:
            mid = self.right.L - 1
        left = self.left.val if self.left else MAX_RANGE
        right = self.right.val if self.right else left
        left = self.left.val if self.left else right

        if mid >= R:
            if self.left:
                left = self.left._addInterval(max(L, self.L), R, length)
        elif mid < L:
            if self.right:
                right = self.right._addInterval(L, min(R, self.R), length)
        else:
            if self.left:
                left = self.left._addInterval(max(L, self.L), mid, length)
            if self.right:
                right = self.right._addInterval(mid + 1, min(R, self.R), length)

        if not self.right:
            right = left
        elif not self.left:
            left = right

        self.val = left if left == right else MAX_RANGE
        return self.val

    def query(self, query: int) -> int:
        if not self:
            return -1

        if self.L == self.R:
            return self.val if self.val != MAX_RANGE else -1

        if self.val != MAX_RANGE:
            return self.val
        
        mid = self.left.R if self.left else self.right.L - 1 if self.right else (self.L + self.R) // 2

        if query <= mid:
            return self.left.query(query) if self.left else -1
        else:
            return self.right.query(query) if self.right else -1

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