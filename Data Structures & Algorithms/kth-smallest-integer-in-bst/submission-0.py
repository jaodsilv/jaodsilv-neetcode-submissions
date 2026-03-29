# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def count(self, root: Optional[TreeNode], k: int, counted: int):
        if root.left is not None:
            counted, val = self.count(root.left, k, counted)
            if counted >= k:
                return (counted, val)
        counted += 1
        if counted >= k:
            return (counted, root.val)
        if root.right is not None:
            counted, val = self.count(root.right, k, counted)
            if counted >= k:
                return (counted, val)
        return (counted, None)

            
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Initially I don't know how many elements there is in the tree, let's start by counting, perhaps creating a counting tree
        # We can count using a dfs to the left and stop when we hit k elements
        _, val = self.count(root, k, 0)
        return val