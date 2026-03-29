# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Let's count the number of elements, so we know which one to remove
        if head is None or (head.next is None and n == 1):
            return None

        count = 0
        node = head
        while node:
            count += 1
            node = node.next
        # We have to remove the element of index count-n th element
        count -= (n)
        node = head
        print(count)
        if count == 0:
            head = head.next
        else:
            while count > 1 and node.next:
                count -= 1
                node = node.next
            if node and node.next:
                node.next = node.next.next
        return head