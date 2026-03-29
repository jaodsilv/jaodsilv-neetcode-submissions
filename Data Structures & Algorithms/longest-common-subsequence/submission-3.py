class Node:
    def __init__(self, L, R, left=None, right=None) -> None:
        self.val = 0
        self.L = L
        self.M = (L+R)//2
        self.R = R
        self.left = left
        self.right = right

    @property
    def leaf(self) -> bool:
        return self.L == self.R

class SegmentationTree:
    def __init__(self, N) -> None:
        self.root = self.buildTree(0, N-1)

    def buildTree(self, L, R) -> Node:
        if L == R:
            return Node(L, L)
        M = (L+R) // 2
        left = self.buildTree(L, M)
        right = self.buildTree(M+1, R)
        return Node(L, R, left, right)

    def update(self, index, val, node = None):
        if node is None:
            node = self.root
        
        if node.L == node.R == index:
            node.val = val
            return
        if index <= node.M:
            self.update(index, val, node.left)
        else: # index > node.M:
            self.update(index, val, node.right)

        node.val = max(node.left.val, node.right.val)

    def query(self, L, R, node=None):
        if node is None:
            node = self.root

        if R <= node.M:
            return self.query(L, R, node.left)
        if L > node.M:
            return self.query(L, R, node.right)
        return max(self.query(L, node.M, node.left), self.query(node.M+1, R, node.right))

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) == 1:
            return 1 if text1[0] in text2 else 0
        if len(text2) == 1:
            return 1 if text2[0] in text1 else 0

        '''
          p s n w
        v[4 3 2 1 0]
        o[3 3 2 1 0]
        z[3 1 0 0 0]
        s[1 1 0 0 0]
        h[0 0 0 0 0]
        -[0 0 0 0 0]
        '''
        if len(text1) > len(text2):
            text1, text2 = text2, text1
        dp = [0]*(len(text1) + 1)

        for i in range(len(text2)-1, -1, -1):
            dpPrev = dp
            dp = [0]*(len(text1) + 1)

            for j in range(len(text1)-1, -1, -1):
                if text1[j] == text2[i]:
                    dp[j] = dpPrev[j+1] + 1
                else:
                    dp[j] = max(dpPrev[j], dp[j+1])
        return dp[0]