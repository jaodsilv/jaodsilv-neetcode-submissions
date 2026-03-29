# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        tree:     1
                2   3
                      4
        preorder: 1, 2, 3, 4
        inorder: 2, 1, 3, 4
        '''

        revMapPreorder = {v: i for i, v in enumerate(preorder)}
        revMapInorder = {v: i for i, v in enumerate(inorder)}

        root = TreeNode(preorder[0])
        indexInorder = revMapInorder[preorder[0]]
        def dfs(node, lIn, rIn):
            v = node.val
            # Test if there is a left node:
                # Preorder: A child node never comes before a parent node, however levels are not guaranteed
                # In the preorder it must come right after the root
                # If it has a left node, in the preorder it always come right after it
                # in the inorder, it must come before
            
            iPre = revMapPreorder[v]
            if rIn == lIn:
                # Then it has no children
                return iPre

            iIn = revMapInorder[v] # Usually about the middle of the range [lIn, rIn]
            print(v, iPre, lIn, iIn, rIn)
            if iIn > lIn: # There are nodes to the left
                vCand = preorder[iPre+1]
                print(f'{v} -l> {vCand}')
                left = TreeNode(vCand)
                node.left = left
                iPre = dfs(left, lIn, iIn - 1)
                print(iPre)

            if iIn < rIn: # There are nodes to the right
                vCand = preorder[iPre + 1]
                print(f'{v} -r> {vCand}')
                right = TreeNode(vCand)
                node.right = right
                iPre = dfs(right, iIn + 1, rIn)
            return iPre

        dfs(root, 0, len(inorder) - 1)
        return root