from collections import deque
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        j = 0
        queue = deque()
        for i in range(m+n):
            if queue:
                if i < m:
                    queue.append(nums1[i])
                if j < n and nums2[j] < queue[0]:
                    nums1[i] = nums2[j]
                    j += 1
                else:
                    nums1[i] = queue.popleft()
            elif i >= m or nums1[i] > nums2[j]:
                if i < m:
                    queue.append(nums1[i])
                nums1[i] = nums2[j]
                j += 1
    
                