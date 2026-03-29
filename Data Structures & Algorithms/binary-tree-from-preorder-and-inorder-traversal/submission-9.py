# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        preorder:[1,2,-,-,3,-,4]
         inorder:[-,2,-,1,-,3,4]
        '''
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        inMap = {}
        for i in range(len(preorder)):
            inMap[inorder[i]] = i

        l = 0
        r = len(preorder) - 1
        def backtrack(in1: int, in3: int, pre1: int) -> Optional[TreeNode]:
            if in3 < in1:
                return None
            val = preorder[pre1]
            if in3 == in1:
                return TreeNode(val)


            # Left subtree goes from in1 to in2-1
            # size of left subtree is in2-1 - in1 + 1 = in2-in1
            # Right subtree goes from in2+1 to in3
            # size of right subtree is in3-in2+1+1 = in3-in2+2
            in2 = inMap[val]
            # Left subtree goes from pre1+1 to pre1+in2-in1
            # Right subtree goes from pre1+in2-in1+1 to pre1-in1+in3+2==pre3
            left = backtrack(in1, in2-1, pre1+1)
            right = backtrack(in2+1, in3, pre1+1+in2-in1)
            return TreeNode(val, left, right)


        return backtrack(0, len(preorder) - 1, 0)