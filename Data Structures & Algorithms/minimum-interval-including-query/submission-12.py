class SegmentTreeNode:
    __infinity = 10001
    def __init__(self, L, R):
        self.val = SegmentTreeNode.__infinity
        self.lazy = SegmentTreeNode.__infinity
        self.L = L
        self.R = R
        self.M = (L + R) // 2
        self.left = None
        self.right = None
        if self.L != self.R:
            self.left = SegmentTreeNode(L, self.M)
            self.right = SegmentTreeNode(self.M + 1, R)

    def propagate(self):
        if self.lazy != SegmentTreeNode.__infinity:
            self.val = min(self.val, self.lazy)
            if self.L != self.R:
                self.left.lazy = min(self.lazy, self.left.lazy)
                self.right.lazy = min(self.lazy, self.right.lazy)
            self.lazy = SegmentTreeNode.__infinity
        return self.val

    def update(self, L, R, val):
        self.propagate()
        if self.L >= L and self.R <= R:
            self.lazy = min(self.lazy, val)
            return self.propagate()

        lVal = None
        rVal = None
        if R <= self.M:
            lVal = self.left.update(L, R, val)
            rVal = self.right.propagate()
        elif L > self.M:
            lVal = self.left.propagate()
            rVal = self.right.update(L, R, val)
        else:
            lVal = self.left.update(L, R, val)
            rVal = self.right.update(L, R, val)
        self.val = min(lVal, rVal)
        return self.val
    
    def query(self, i):
        self.propagate()
        if self.L == self.R:
            return self.val if self.val < SegmentTreeNode.__infinity else -1
        if i <= self.M:
            return self.left.query(i)
        else:
            return self.right.query(i)

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        points = sorted(set(queries + [i[0] for i in intervals] + [i[1] for i in intervals]))
        pointsMap = {}
        for i, p in enumerate(points):
            pointsMap[p] = i
        intervals = [[pointsMap[l], pointsMap[r], r - l + 1] for l, r in intervals]
        queries = [pointsMap[q] for q in queries]
        segTree = SegmentTreeNode(0, len(points) - 1)
        for l, r, val in intervals:
            segTree.update(l, r, val)
        res = []
        for q in queries:
            res.append(segTree.query(q))
        return res
        

