# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        def backtracking(node):
            if node is None:
                return []
            r = backtracking(node.left)
            r.append(node.val)
            return r + backtracking(node.right)
        return backtracking(root)
        # Inorder means left, middle, right
        # If 