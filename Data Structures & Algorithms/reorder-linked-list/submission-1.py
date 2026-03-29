# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque

class Solution:

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return None
        
        def printLL(node):
            while node:
                print(node.val, end='->')
                node = node.next
            print('None')
        # Let's use slow and fast pointers to ge to the middle of the list
        slow, fast, prev = head, head, None
        while fast and fast.next:
            slow, prev = slow.next, slow
            fast = fast.next.next
        if fast:
            slow, prev = slow.next, slow
        
        prev.next = None
        #else:
        # printLL(head)
        # printLL(slow)
        # slow is in the middle, now we revert the middle and beyond
        head2 = slow
        prev = None
        while slow:
            slow.next, slow, prev = prev, slow.next, slow
            #print('slow.next, slow, prev = ', slow.next, slow.val, prev.val)
        #print('prev, slow.next = ', prev.val, slow.next.val if slow.next else 'None')
        #slow.next, slow = prev, slow.next
        #slow.next = prev

        #printLL(head)
        #printLL(prev)
        head2 = prev

        # now we merge them
        node1 = head
        node2 = head2
        while node1 and node2:
            node1.next, node2.next, node1, node2 = node2, node1.next, node1.next, node2.next
        if node1:
            node1.next = None
        elif node2:
            node2.next = None

        '''
        Solution 1:
        '''
        '''
        while node:
            lld.append(node)
            node = node.next
        node = lld.popleft()
        # print(lld)
        while lld:
            node.next = lld.pop()
            node = node.next
            if lld:
                node.next = lld.popleft()
                node = node.next
        node.next = None

        print(head)
        return head
        '''