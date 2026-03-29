# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root or (not root.left and not root.right):
            return True
        
        def isValidAndGetMinMax(root):
            val = root.val
            minVal, maxVal = val, val
            if root.left:
                minLeft, maxLeft = isValidAndGetMinMax(root.left)
                if maxLeft is None or maxLeft >= root.val:
                    return None, None
                minVal = min(minVal, minLeft)
                maxVal = max(maxVal, maxLeft)
            if root.right:
                minRight, maxRight = isValidAndGetMinMax(root.right)
                if minRight is None or minRight <= root.val:
                    return None, None
                minVal = min(minVal, minRight)
                maxVal = max(maxVal, maxRight)
            return minVal, maxVal
        if root.left:
            minLeft, maxLeft = isValidAndGetMinMax(root.left)
            if maxLeft is None or maxLeft >= root.val:
                return False
        if root.right:
            minRight, maxRight = isValidAndGetMinMax(root.right)
            if minRight is None or minRight <= root.val:
                return False
        return True