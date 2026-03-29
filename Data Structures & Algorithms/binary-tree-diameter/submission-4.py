# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node):
            if not node:
                return (0, 0)
            maxDiam = 0
            currLeg = 0
            dL, legL = dfs(node.left)
            dR, legR = dfs(node.right)
            currLeg = max(legL, legR) + 1
            maxDiam = max(dL, dR, legL+legR)
            return (maxDiam, currLeg)
        return dfs(root)[0]
