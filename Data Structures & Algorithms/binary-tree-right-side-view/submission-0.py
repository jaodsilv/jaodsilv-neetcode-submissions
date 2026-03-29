# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # We must do something similar to a dfs preorder but going to the right first and remembering the depth of the tree
        if root is None:
            return []
        nodes = [(root, 0)]
        res = []
        minH = 0
        while nodes:
            node, h = nodes.pop()
            if h == minH:
                res.append(node.val)
                minH += 1
            if node.left:
                nodes.append((node.left, h + 1))
            if node.right:
                nodes.append((node.right, h + 1))
        return res
