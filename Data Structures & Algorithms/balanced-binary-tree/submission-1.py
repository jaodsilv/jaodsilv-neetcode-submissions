# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def _heights(self, node):
        if node is None:
            return 0
        left = self._heights(node.left)
        right = self._heights(node.right)
        if left is None or right is None:
            return None
        if abs(left - right) <= 1:
            return max(left, right) + 1
        else:
            return None


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        h = self._heights(root)
        return h is not None
