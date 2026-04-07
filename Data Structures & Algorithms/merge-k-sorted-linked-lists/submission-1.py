# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def merge(L1, L2):
            root = ListNode()
            node = root
            while L1 and L2:
                if L1.val < L2.val:
                    node.next = L1
                    node = L1
                    L1 = L1.next
                else:
                    node.next = L2
                    node = L2
                    L2 = L2.next
            if L1:
                node.next = L1
            else:
                node.next = L2
            return root.next

        base = None
        for LL in lists:
            if not LL:
                continue
            if base is None:
                base = LL
                continue
            base = merge(base, LL)
        return base