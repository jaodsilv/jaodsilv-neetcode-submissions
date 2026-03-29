# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        t = l1.val + l2.val
        carry1 = t >= 10
        if carry1:
            t -= 10
        head = ListNode(t)
        node = head
        while l1.next and l2.next:
            l1 = l1.next
            l2 = l2.next
            t = l1.val + l2.val
            if carry1:
                t += 1
            carry1 = t >= 10
            if carry1:
                t -= 10
            next = ListNode(t)
            node.next = next
            node = next
            
        remaining = l1 if l1.next else l2
        while remaining.next:
            remaining = remaining.next
            t = remaining.val
            if carry1:
                t += 1
            carry1 = t >= 10
            if carry1:
                t -= 10
            next = ListNode(t)
            node.next = next
            node = next

        if carry1:
            next = ListNode(1)
            node.next = next
        return head