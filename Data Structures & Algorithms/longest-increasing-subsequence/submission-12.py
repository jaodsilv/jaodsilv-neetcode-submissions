class Node:
    def __init__(self, L, R):
        self.val = 0
        self.L, self.R = L, R
        self.M = (L + R) // 2
        self.left = self.right = None
        if L != R:
            self.left = Node(L, self.M)
            self.right = Node(self.M + 1, R)

    def update(self, I, val):
        if not self.left or not self.right:
            self.val = val
            return val
        if I <= self.M:
            self.val = max(self.left.update(I, val), self.val)
        else:
            self.val = max(self.right.update(I, val), self.val)
        return self.val
    
    def query(self, L, R):
        if R < L:
            return 0
        if not self.left or not self.right:
            return self.val
        if R <= self.M:
            return self.left.query(L, R)
        elif L > self.M:
            return self.right.query(L, R)
        return max(self.left.query(L, R), self.right.query(L, R))
        
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        compressList = sorted(list(set(nums)))
        compressMap = {v: i for i, v in enumerate(compressList)}
        compress = [compressMap[n] for n in nums]
        nodes = Node(0, len(compressList) - 1)

        maxVal = 0
        for n in compress:
            val = nodes.query(0, n-1) + 1
            nodes.update(n, val)
            maxVal = max(maxVal, val)
        return maxVal

