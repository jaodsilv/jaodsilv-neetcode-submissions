# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # First let's find the path to p and q
        def getPath(root, node):
            if root.val == node.val:
                return [root]
            if root.left:
                left = getPath(root.left, node)
                if left:
                    left.append(root)
                    return left
            if root.right:
                right = getPath(root.right, node)
                if right:
                    right.append(root)
                    return right
            return []
        pPath = getPath(root, p)
        #print([node.val for node in pPath])
        qPath = getPath(root, q)
        #print([node.val for node in qPath])
        qSet = set([node.val for node in qPath])
        for node in pPath:
            if node.val in qSet:
                return node
        return root

