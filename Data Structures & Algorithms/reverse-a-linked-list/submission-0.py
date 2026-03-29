# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        stack = []
        while head:
            stack.append(head)
            head = head.next
        head = stack[-1]
        node = head
        prev = None
        while len(stack) > 0:
            node = stack.pop()
            if prev is not None:
                prev.next = node
            prev = node
        prev.next = node
        node.next = None
        # print('stack', stack, node.val, prev.val)
        return head