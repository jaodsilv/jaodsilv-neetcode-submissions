import bisect

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Tree
                              1
               2                   3
       4               5                  7
   8              L1      11           14     15
Pre-order
[1, 2, 4, 8, -, 5, L1, 11, 3, -, -, -, 7, 14, 15]
In-Order
[8, 4, -, 2, L1, 5, 11, 1, -, -, -, 3, 14, 7, 15]
[1, 2, 4, 8, 5, L1, 11, 3, 7, 14, 15]
[8, 4, 2, L1, 5, 11, 1, 3, 14, 7, 15]
'''
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
            Let's rebuild the tree based on the supposed relationships
            Both arrays might contain gaps, as the tree is not necessarily balanced
            When a subtree to the left or right of the node is missing, it create gaps:
                LEFT:
                    - Pre-Order:
                    - immediatly After its parent
                    - The last element or immediatly before the next subtree that goes to the right
                    - In-Order: 
                    - At the beginning or immediatly After the first parent that goes to the left (i, e., its child is the right child)
                    - immediatly before its parent
                RIGHT:        
                    - Pre-Order:
                    - immediatly After its left sibling or its parent
                    - The last element or immediatly before the next subtree that goes to the right
                    - In-Order: 
                    - immediatly After its parent
                    - The last element or immediatly before the first parent to the right
            Consider we are at a node, at p in the preorder, and i in the inorder
            If There ONLY a subtree to the left, then both:
                1. PREORDER:
                    1. It will be at pl = p + 1
                    2. pLLast + 1 is a right uncle
                2. INORDER:
                    1. It will be at il < i
                    2. iLLast + 1 = ppi
            If there is a subtree to the right we have:
                1. PREORDER
                    1. It will be at pr = p + 1
                2. INORDER
                    1. It will be at i < ir
            If there are both subtrees:
                1. PREORDER
                    1. Left child pl = p+1
                    2. Right Child will be pr > pl > p
                    3. pr = pLLast + 1
                2. INORDER
                    1. il < i < ir
                    2. iLLast + 1 == i
                    3. iRLast + 1 == parent[i]
            If there are neither:
                1. PREORDER
                    1. p+1 will be a sibling or an uncle
                2. INORDER
                    1. i+1


        p[0] is surelly the root
        Let's find its value in the inorder
        '''
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


        def buildChildren(node, revIndex, parentL):#values, inIndexes, preIndexes) -> int:
            iPre, iIn = revIndex[node.val]
            if iPre == len(preorder) - 1:
                return iPre
            # parentL is the value of the first parent up in the tree that is a parent of a left child
            # parentR it the value of the first parent up in the tree that is a parent of a right child

            # every left subtree node has inorder index < iIn
            # every right subtree node has inorder index > iIn
            # every node out of the current subtree is < inorder parentL or > previous parentR

            # If it has a left child
            lastPre = iPre
            childPreCand = iPre + 1
            childCand = preorder[childPreCand]
            childInCand = revIndex[childCand][1]
            # If it is lower, it is surely it left child
            if childInCand < iIn:
                parents[childCand] = node.val
                node.left = TreeNode(childCand)
                lastPre = buildChildren(node.left, revIndex, iIn)
                # Check if there is also a right child
                # Last of the left + 1 in the preorder should the right child, if it exists
                if lastPre == len(preorder) - 1:
                    return lastPre
                childPreCand = lastPre + 1
                childCand = preorder[childPreCand]
                childInCand = revIndex[childCand][1]
                if parentL == -1 or childInCand < parentL:
                    node.right = TreeNode(childCand)
                    lastPre = buildChildren(node.right, revIndex, parentL)

            # Other wise it can be either a right child or a different arm in a higher level.
            # In this case we check against its parent
            # If childInCand > parentIn, then it is a different arm, otherwise it is a right child
            elif parentL == -1 or childInCand < parentL:
                node.right = TreeNode(childCand)
                lastPre = buildChildren(node.right, revIndex, parentL)
            return lastPre

        v = preorder[0]
        values = set(preorder)
        inIndexes = set(range(len(inorder)))
        preIndexes = set(range(len(inorder)))
        root = TreeNode(v)
        parents = {0: -1}
        buildChildren(root, revIndex, -1)
        return root
