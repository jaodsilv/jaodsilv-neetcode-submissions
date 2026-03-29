# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        indexMap = {}
        for i in range(len(inorder)):
            indexMap[inorder[i]] = i

        def build(l, r) -> Optional[TreeNode]:
            if r <= l:
                return None
            i = indexMap[preorder[0]]
            root = TreeNode(preorder[0])
            root.left = self.buildTree(preorder[1:i+1], inorder[:i])
            root.right = self.buildTree(preorder[i+1:], inorder[i+1:])
            return root
        return build(0, len(preorder))
