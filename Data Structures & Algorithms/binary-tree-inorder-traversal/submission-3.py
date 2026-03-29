# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Morries Traversal
        node = root
        res = []
        while node:
            if not node.left:
                res.append(node.val)
                node = node.right
            else:
                prev = node.left
                while prev.right and prev.right != node:
                    prev = prev.right
                if prev.right is None:
                    prev.right = node
                    node = node.left
                else:
                    prev.right = None
                    res.append(node.val)
                    node = node.right
        return res      
