class SegmentTreeNode:
    minVal = -1001

    def __init__(self, n = None, L = None, R = None):
        if L is None or R is None:
            if n is None:
                return
            L = 0
            R = n - 1
        self.L = L
        self.R = R
        self.value = 0
        if L == R:
            self.M = L
        else:
            M = (L + R) // 2
            self.M = M
            self.left = SegmentTreeNode(L = L, R = M)
            self.right = SegmentTreeNode(L = M+1, R = R)

    def update(self, index, val):
        if self.L == self.R == index:
            self.value = val
        else:
            if index > self.M:
                self.right.update(index, val)
            else:
                self.left.update(index, val)
            self.value = max(self.left.value, self.right.value)

    def query(self, L, R):
        if L > R:
            return 0

        if self.L == L and self.R == R:
            return self.value
        if L > self.M:
            return self.right.query(L, R)
        elif R <= self.M:
            return self.left.query(L, R)
        else:
            return max(self.left.query(L, self.M), self.right.query(self.M + 1, R))

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # compress nums so we don't have gaps between the numbers
        # O(nlogn)
        sortedNums = sorted(set(nums))
        # O(n)
        sortedMap = {num: i for i, num in enumerate(sortedNums)}
        # O(n)
        compressed = [sortedMap[num] for num in nums]

        n = len(compressed)
        segTree = SegmentTreeNode(n)
        lis = 0
        for num in compressed:
            curLis = segTree.query(0, num - 1) + 1
            segTree.update(num, curLis)
            lis = max(lis, curLis)
        return lis