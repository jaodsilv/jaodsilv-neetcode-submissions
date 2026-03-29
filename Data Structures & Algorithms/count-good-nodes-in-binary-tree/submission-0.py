# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Store greatest value
        count = 1 # root is always a good node
        
        stack = [(root, root.val)]
        while stack:
            node, target = stack.pop()
            if node.right:
                if node.right.val >= target:
                    count += 1
                stack.append((node.right, max(target, node.right.val)))
            if node.left:
                if node.left.val >= target:
                    count += 1
                stack.append((node.left, max(target, node.left.val)))
        return count
