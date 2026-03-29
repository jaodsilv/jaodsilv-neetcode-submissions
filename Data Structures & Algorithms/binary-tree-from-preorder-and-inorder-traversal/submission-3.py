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

        '''
        #preorder = [1,2,3,4], inorder = [2,1,3,4]
        0, 4, 0, 4 =>
        i = 1, lpre = 1, rpre = 2, lin = 1
        Left Node:
            left node length should be i - lin
            lpre = lpre + 1, rpre = lpre + 1 + i - lin
            lin = lin, rin = i
        Right Node:
            right node length should be rin - i
            lpre = lpre + 1 + i - lin, rpre = rpre
            lin = i + 1, rin = rin
        '''
        def build(lpre, rpre, lin, rin) -> Optional[TreeNode]:
            if rpre <= lpre:
                return None
            i = indexMap[preorder[lpre]]
            root = TreeNode(preorder[lpre])
            root.left = build(lpre+1, lpre + 1 + i - lin, lin, i)
            root.right = build(lpre + 1 + i - lin, rpre, i+1, rin)
            return root
        return build(0, len(preorder), 0, len(preorder))
