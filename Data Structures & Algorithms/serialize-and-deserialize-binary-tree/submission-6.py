# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return '.'
        stack = [root]
        # queue = deque([root])
        res = []
        # while queue:
        while stack:
            node = stack.pop()
            if node is None:
                res.append('.')
            else:
                res.append(str(node.val))
                stack.append(node.right)
                stack.append(node.left)
        while res and res[-1] == '.':
            res.pop()
        return ','.join(res)


    def _deserialize(self, data:list[str], i: int) -> tuple:
        if i >= len(data) or data[i] == '.':
            return None, i + 1
        node = TreeNode(int(data[i]))
        i += 1
        left, i = self._deserialize(data, i)
        right, i = self._deserialize(data, i)
        node.left = left
        node.right = right
        return node, i


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # print(data)
        node, _ = self._deserialize(data.split(','), 0)
        return node