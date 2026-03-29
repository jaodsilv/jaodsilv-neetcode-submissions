# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return
        # Let's find the middle with the fast and slow pointers
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow
        stack = []
        while slow:
            stack.append(slow)
            slow = slow.next

        # Now let's do the reordering

        left = head
        right = None
        while stack:
            right = stack.pop()
            ln = left.next
            left.next = right
            right.next = ln
            left = ln
        right.next = None