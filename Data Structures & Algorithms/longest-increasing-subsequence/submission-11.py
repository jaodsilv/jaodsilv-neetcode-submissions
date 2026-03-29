class Node:
    def __init__(self, val, L, R, left, right):
        self.val = val
        self.L = L
        self.M = (L + R) // 2
        self.R = R
        self.left = left
        self.right = right

    def update(self, point, val):
        if self.L == self.R:
            self.val = val
            return
        if point <= self.M:
            self.left.update(point, val)
        else:
            self.right.update(point, val)
        self.val = max(self.left.val, self.right.val)

    def query(self, L, R):
        if self.L == L and self.R == R:
            return self.val
        if R <= self.M:
            return self.left.query(L, R)
        elif L > self.M:
            return self.right.query(L, R)
        else:
            return max(self.left.query(L, self.M), self.right.query(self.M + 1, R))

class SegTree:
    def __init__(self, N):
        self.root = self._buildTree(0, N-1)
    def _buildTree(self, L, R):
        left = None
        right = None
        M = (L + R) // 2
        if L != R:
            left = self._buildTree(L, M)
            right = self._buildTree(M + 1, R)
        return Node(0, L, R, left, right)
    def update(self, point, val):
        self.root.update(point, val)

    def query(self, L, R) -> int:
        return self.root.query(L, R)

        
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sortedNums = sorted(set(nums))
        compressMap = {n: i for i, n in enumerate(sortedNums)}
        nums = [compressMap[n] for n in nums]

        segTree = SegTree(len(sortedNums))

        maxLen = 0
        for n in nums:
            val = segTree.query(0, n-1) if n > 0 else 0
            segTree.update(n, val + 1)
            maxLen = max(maxLen, val + 1)
        return maxLen
