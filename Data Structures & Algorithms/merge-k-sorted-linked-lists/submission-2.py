import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)

        heap = []
        for LL in lists:
            while LL:
                heapq.heappush(heap, LL.val)
                LL = LL.next
        
        root = ListNode()
        tail = root
        while heap:
            tail.next = ListNode(heapq.heappop(heap))
            tail = tail.next
        return root.next