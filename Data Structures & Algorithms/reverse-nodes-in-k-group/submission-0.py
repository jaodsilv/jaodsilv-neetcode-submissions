# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        nodes = [None]*k
        # Fill
        node = head
        for i in range(k):
            if node is None:
                return head
            nodes[i] = node
            node = node.next
        head = nodes[-1]
        tail = nodes[0]
        for i in range(k-1):
            nodes[i+1].next = nodes[i]
        while node:
            for i in range(k):
                if node is None:
                    tail.next = nodes[0]
                    return head
                nodes[i] = node
                node = node.next
            # There are enough items
            
            tail.next = nodes[-1]
            tail = nodes[0]
            for i in range(k-1):
                nodes[i+1].next = nodes[i]
        tail.next = None
        return head