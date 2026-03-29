# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def maxSum(root):
            # Output is the pair (max sum below this node, max leg sum including the current node)
            if not root:
                #print('None', 0, 0)
                return (0, 0)
            if not root.left and not root.right:
                #print('leaf', root.val)
                return (root.val, root.val)

            #print('Node', root.val)
            maxBelow, maxLeg = root.val, root.val

            if root.left:
                maxBelowLeft, maxLegLeft = maxSum(root.left)
                maxLeg = max(maxLeg, maxLegLeft + root.val)
                maxBelow = max(maxBelowLeft, maxLeg)

            if root.right:
                maxBelowRight, maxLegRight = maxSum(root.right)
                maxBelow = max(maxBelow, maxLeg, maxBelowRight, maxLeg + maxLegRight)
                maxLeg = max(maxLeg, maxLegRight + root.val)
            
            return maxBelow, maxLeg
        return maxSum(root)[0]