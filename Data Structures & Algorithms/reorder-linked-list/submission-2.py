# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None or head.next.next is None:
            return

        def printLL(head):
            print('[', end='')
            while head.next is not None:
                print(head.val, end=', ')
                head = head.next
            print(f'{head.val}]')

        # Using fast and slow pointers to find the middle
        slow, fast = head, head
        prev = slow
        while fast is not None:
            slow, fast, prev = slow.next, fast.next, slow
            if fast:
                fast = fast.next
        prev.next = None
        #printLL(slow)

        prev = slow # prev = 6
        slow = slow.next # slow = 8
        prev.next = None # 6 -> None
        while slow is not None:
            slow.next, slow, prev = prev, slow.next, slow # 8 -> 6, 

        #printLL(prev)
        #printLL(head)

        node = head
        while node is not None and prev is not None:
            nextNode = node.next
            nextPrev = prev.next
            node.next = prev
            prev.next = nextNode
            node = nextNode
            prev = nextPrev