import bisect
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def median(nums):
            if len(nums) == 0:
                return 0
            if len(nums) == 1:
                return nums[0]
            if len(nums) % 2 == 1:
                return nums[len(nums)//2]
            else:
                return (nums[len(nums)//2] + nums[(len(nums) // 2 - 1)]) / 2

        # Brute force solution: O(n*log(n))
        merged = sorted(nums1 + nums2)
        return median(merged)
