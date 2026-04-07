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
        for i, LL in enumerate(lists):
            if LL:
                heapq.heappush(heap, (LL.val, i, LL))

        root = ListNode()
        tail = root
        while heap:
            _, i, LL = heap[0]
            tail.next = LL
            tail = LL
            LL = LL.next
            if LL:
                heapq.heapreplace(heap, (LL.val, i, LL))
            else:
                heapq.heappop(heap)
        return root.next