"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        copyHead = Node(head.val)
        copyNode = copyHead
        node = head
        copiedNodes = {head: copyHead}
        while node.next is not None:
            newNode = None
            if node.next in copiedNodes:
                newNode = copiedNodes[node.next]
            else:
                newNode = Node(node.next.val)
                copiedNodes[node.next] = newNode
            copyNode.next = newNode

            if node.random in copiedNodes:
                newNode = copiedNodes[node.random]
            elif node.random is not None:
                newNode = Node(node.random.val)
                copiedNodes[node.random] = newNode
            else:
                newNode = None
            copyNode.random = newNode

            copyNode = copyNode.next
            node = node.next
        if node.random is not None:
            copyNode.random = copiedNodes[node.random]
        return copyHead
