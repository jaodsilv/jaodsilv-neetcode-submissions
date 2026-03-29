# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        Let's do it recursively
        We may store the max diameter of the left, max diameter of the right,
        the max leg of the left, the max leg of the right
        '''
        def dfs(node):
            if node.left is None and node.right is None:
                return (0, 0)
            
            maxLengthL, maxLengthR = 0, 0
            maxDiameter = 0

            if node.left:
                maxLengthL, maxDiameter = dfs(node.left)
            else:
                maxLengthL = -1

            if node.right:
                maxLengthR, maxDiameterR = dfs(node.right)
                maxDiameter = max(maxDiameter, maxDiameterR)
            else:
                maxLengthR = -1

            return (max(maxLengthR, maxLengthL) + 1, max(maxDiameter, maxLengthL + maxLengthR + 2))
        return dfs(root)[1]