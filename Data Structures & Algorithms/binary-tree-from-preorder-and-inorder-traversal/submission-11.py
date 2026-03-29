# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        [5,3,6,1,4,null,7,null,2]
                                       5
                                3               6
                            1       4       null    7
                        null  2
        '''
        head = TreeNode(-1001)
        curr = head
        i, j = 0, 0
        while i < len(preorder):
            curr.right = TreeNode(preorder[i], right = curr.right)
            curr = curr.right
            i+=1
            while i < len(preorder) and curr.val != inorder[j]:
                curr.left = TreeNode(preorder[i], right=curr)
                curr = curr.left
                i+=1
            # We have now preorder[i] == inorder[j]
            j+=1
            while curr.right and j < len(inorder) and inorder[j] == curr.right.val:
                # There is no right child to the last left pointed
                # Then go up in the chain, cleaning up the false right children
                j += 1
                prev = curr.right
                curr.right = None
                curr = prev

            # else: # if inorder[j] != curr.val:
                # There is a right child to the last left built
        return head.right
