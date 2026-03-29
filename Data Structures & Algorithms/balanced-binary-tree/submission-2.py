# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # DFS
        def dfs(node) -> int | None:
            if not node:
                return 0
            L = dfs(node.left)
            R = dfs(node.right)

            if L is None or R is None or abs(R - L) > 1:
                return None
            else:
                return max(R, L) + 1
            
        return False if dfs(root) is None else True
                
