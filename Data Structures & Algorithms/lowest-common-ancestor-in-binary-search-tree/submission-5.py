from enum import Enum
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # make p the smaller
        if p.val > q.val:
            p, q = q, p

        node = root
        while not (p.val <= node.val <= q.val):
            if node.val < p.val:
                # Both to the right
                node = node.right
            if node.val > q.val:
                # Both to the left
                node = node.left
            # One for each side
        return node
