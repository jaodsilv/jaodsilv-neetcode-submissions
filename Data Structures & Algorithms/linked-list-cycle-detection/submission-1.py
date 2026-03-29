# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        visited = set()
        node = head
        while node.next is not None:
            if node in visited:
                return True
            visited.add(node)
            node = node.next
        return False