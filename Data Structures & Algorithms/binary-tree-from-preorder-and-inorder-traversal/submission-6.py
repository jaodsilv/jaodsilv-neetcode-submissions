import bisect

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        revIndex = {}
        for i in range(len(preorder)):
            pre = preorder[i]
            if pre in revIndex:
                revIndex[pre][0] = i
            else:
                revIndex[pre] = [i, -1]
            ino = inorder[i]
            if ino in revIndex:
                revIndex[ino][1] = i
            else:
                revIndex[ino] = [-1, i]


        def buildChildren(node, revIndex, parentL):
            iPre, iIn = revIndex[node.val]
            lastPre = iPre
            if iPre == len(preorder) - 1:
                return lastPre
            childPreCand = iPre + 1
            childCand = preorder[childPreCand]
            childInCand = revIndex[childCand][1]
            if childInCand < iIn:
                node.left = TreeNode(childCand)
                lastPre = buildChildren(node.left, revIndex, iIn)
                if lastPre == len(preorder) - 1:
                    return lastPre
                childPreCand = lastPre + 1
                childCand = preorder[childPreCand]
                childInCand = revIndex[childCand][1]
                if parentL == -1 or childInCand < parentL:
                    node.right = TreeNode(childCand)
                    lastPre = buildChildren(node.right, revIndex, parentL)
            elif parentL == -1 or childInCand < parentL:
                node.right = TreeNode(childCand)
                lastPre = buildChildren(node.right, revIndex, parentL)
            return lastPre

        v = preorder[0]
        root = TreeNode(v)
        buildChildren(root, revIndex, -1)
        return root
