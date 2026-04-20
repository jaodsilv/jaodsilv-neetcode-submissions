class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        i = 0
        while i < m:
            if nums1[i] > nums2[0]:
                nums1[i], nums2[0] = nums2[0], nums1[i]
                k = 1
                while k < len(nums2) and nums2[k] < nums2[k-1]:
                    nums2[k], nums2[k-1] = nums2[k-1], nums2[k]
                    k += 1
            i += 1
        for i in range(n):
            nums1[i+m] = nums2[i]
    
                