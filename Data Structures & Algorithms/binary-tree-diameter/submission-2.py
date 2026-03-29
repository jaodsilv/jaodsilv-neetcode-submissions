# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        Let's store a few numbers:
        1. The current height from the root
        2. The current longest leg found
        3. The current length from longestLeg
        4. The current longest Length
        '''
        if root is None or (root.left is None and root.right is None):
            return 0

        # Since it is a tree, it will visit each node only once => O(n)
        def longestLegs(root, dp):
            if root is None:
                return 0

            if root.left is None and root.right is None:
                dp[root] = 0
                return 0

            maxLeg = max(longestLegs(root.left, dp), longestLegs(root.right, dp)) + 1
            dp[root] = maxLeg
            return maxLeg

        def longestPath(root, dp):
            if root is None:
                return -1
            if root.left is None and root.right is None:
                return 0

            return max(longestPath(root.left, dp), longestPath(root.right, dp), dp[root.right] + dp[root.left] + 1)

        dp = {None: -1}
        longestLegs(root, dp)
        return longestPath(root, dp) + 1
