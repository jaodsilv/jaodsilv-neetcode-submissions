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
        if not head:
            return None
        # Let's insert the copied nodes into the original list
        node = head
        while node:
            copy = Node(node.val, node.next, node.random)
            node.next = copy
            node = copy.next
        # Now we make the random point to the copied nodes
        node = head
        while node:
            copy = node.next
            if copy.random:
                copy.random = copy.random.next
            node = copy.next
        # Now all random are pointing to the correct nodes
        # we can split the nodes in nexts
        node = head
        dummyHead = Node(0, node.next)
        copy = dummyHead
        while node: # current node
            # For now, copy is the previous node's copy
            copy.next, node.next = node.next, node.next.next
            copy, node = copy.next, node.next
        return dummyHead.next