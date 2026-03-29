# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # '''Solution 1:'''
        # if head is None:
        #     return False
        # visited = set()
        # node = head
        # while node.next:
        #     if node in visited:
        #         return True
        #     visited.add(node)
        #     node = node.next
        # return False
        '''Solutuion 2:'''
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False