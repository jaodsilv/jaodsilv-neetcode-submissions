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
        res = []

        nodes = [(root, False)]
        while nodes:
            node, mid = nodes.pop()
            if mid:
                res.append(node.val)
            else:
                if node.right:
                    nodes.append((node.right, False))
                nodes.append((node, True))
                if node.left:
                    nodes.append((node.left, False))
            
        return res

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        inorder(root)
        return res
        # Inorder means left, middle, right
        # If 