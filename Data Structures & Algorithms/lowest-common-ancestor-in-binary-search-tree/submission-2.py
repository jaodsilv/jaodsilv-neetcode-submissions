from enum import Enum
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Result(Enum):
    P = 0
    Q = 1

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node) -> TreeNode | None:
            if node is None:
                return None
            if node.val == p.val:
                return node
            if node.val == q.val:
                return node
            
            left = dfs(node.left)
            right = dfs(node.right)
            if left is None:
                return right
            if right is None:
                return left

            # Neither is none, which means one is q, and the other is p
            return node
        return dfs(root)
