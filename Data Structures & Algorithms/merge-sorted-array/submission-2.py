import heapq
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        i = 0
        heapq.heapify(nums2)
        for i in range(m):
            nums1[i] = heapq.heappushpop(nums2, nums1[i])
        for i in range(n):
            nums1[i+m] = heapq.heappop(nums2)
    
                