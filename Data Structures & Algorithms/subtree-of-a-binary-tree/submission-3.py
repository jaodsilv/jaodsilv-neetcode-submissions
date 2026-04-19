# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def getString(node):
            if not node:
                return '.'
            return ',' + str(node.val) + getString(node.left) + getString(node.right)
        
        string = getString(root)
        substring = getString(subRoot)
        return substring in string
