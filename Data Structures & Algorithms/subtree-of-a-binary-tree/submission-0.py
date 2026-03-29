# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        if root is None:
            return False

        def dfs_comparison(node1, node2):
            if node2 and not node1:
                return False
            if node1 and not node2:
                return False
            if not node1 and not node2:
                return True
            if node1.val != node2.val:
                return False
            if node1.val == node2.val:
                return dfs_comparison(node1.left, node2.left) and dfs_comparison(node1.right, node2.right)
            
        def dfs_find_candidates(node1):
            if node1.val == subRoot.val:
                yield node1
            if node1.left is not None:
                left = dfs_find_candidates(node1.left)
                for x in left:
                    yield x
            if node1.right is not None:
                right = dfs_find_candidates(node1.right)
                for x in right:
                    yield x

        candidates = dfs_find_candidates(root)
        for cand in candidates:
            if dfs_comparison(cand, subRoot):
                return True
        return False
