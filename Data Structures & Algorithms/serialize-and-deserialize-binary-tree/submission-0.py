# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ''
        asList = [root]
        i = 0
        while True:
            hasElements = False
            for j in range(i, len(asList)):
                if asList[j] is None:
                    asList.append(None)
                    asList.append(None)
                else:
                    asList.append(asList[j].left)
                    asList.append(asList[j].right)
                    
                    hasElements = hasElements or asList[j].left is not None or asList[j].right is not None
            if not hasElements:
                break
            i = len(asList) // 2
        return ','.join([str(x.val) if x else 'None' for x in asList[:len(asList) // 2]])

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        print(data)
        if len(data) == 0 or data[0] == 'None':
            return None
        data = [int(x) if x != 'None' else None for x in data.split(',')]

        root = TreeNode(data[0])
        data[0] = root
        for i in range(len(data)):
            if 2 * i + 2 < len(data) and data[i] is not None:
                node = data[i]
                left = None if data[2 * i + 1] is None else TreeNode(data[2 * i + 1])
                right = None if data[2 * i + 2] is None else TreeNode(data[2 * i + 2])
                node.left = left
                node.right = right
                data[2 * i + 1] = left
                data[2 * i + 2] = right
        return root