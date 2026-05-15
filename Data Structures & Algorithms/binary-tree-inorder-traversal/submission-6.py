# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Inorder is left, top, right
        if root is None:
            return []
        stack = [(root, False)]
        res = []
        while stack:
            node, leftAdded = stack.pop()
            if leftAdded:
                res.append(node.val)
                if node.right:
                    stack.append((node.right, True))
                    if node.right.left:
                        stack.append((node.right.left, False))
            else:
                stack.append((node, True))
                if node.left:
                    stack.append((node.left, False))

        return res