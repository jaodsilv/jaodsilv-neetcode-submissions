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
        node = head
        while node: # O(n) time
            copy = Node(node.val, node.next, node.random)
            node.next = copy
            node = copy.next
        node = head
        copyHead = node.next
        while node:
            copy = node.next
            if copy.random:
                copy.random = copy.random.next
            node = copy.next

        node = head
        while node:
            copy = node.next
            node.next = copy.next
            node = copy.next
            if node:
                copy.next = node.next
            
        return copyHead
