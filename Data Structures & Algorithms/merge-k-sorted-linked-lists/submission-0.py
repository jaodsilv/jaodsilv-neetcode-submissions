# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def printlist(self, linked):
        print('[', end='')
        while linked is not None:
            print(linked.val, end='')
            if linked.next is not None:
                print(',', end='')
            linked = linked.next
        print(']')

    def merge2Lists(self, left, right):
        root = None
        if left.val > right.val:
            right, left = left, right
        root = left
        while left.next is not None and right is not None:
            if left.next.val <= right.val:
                left = left.next
            else: # left.val > right.val:
                left.next, right = right, left.next
                left = left.next

        if left.next is None and right is not None:
            left.next = right

        return root            

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        result = lists[0]
        for right in lists[1:]:
            result = self.merge2Lists(result, right)
        return result