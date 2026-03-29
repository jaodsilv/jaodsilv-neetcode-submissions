class SegmentTreeNode:
    __infinity = 10001
    def __init__(self, L, R):
        self.val = SegmentTreeNode.__infinity
        self.L = L
        self.R = R
        self.M = (L + R) // 2
        self.left = None
        self.right = None
        if self.L != self.R:
            self.left = SegmentTreeNode(L, self.M)
            self.right = SegmentTreeNode(self.M + 1, R)

    def update(self, L, R, val):
        if self.val <= val:
            return self.val
        if self.L == self.R:
            self.val = val
            return val

        lVal = self.left.val
        rVal = self.right.val
        if R <= self.M:
            lVal = self.left.update(L, R, val)
        elif L > self.M:
            rVal = self.right.update(L, R, val)
        else:
            lVal = self.left.update(L, self.M, val)
            rVal = self.right.update(self.M+1, R, val)
        if lVal == rVal < SegmentTreeNode.__infinity:
            self.val = lVal
        else:
            self.val = SegmentTreeNode.__infinity
        return self.val
    
    def query(self, i):
        if self.val < SegmentTreeNode.__infinity:
            return self.val
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
        

