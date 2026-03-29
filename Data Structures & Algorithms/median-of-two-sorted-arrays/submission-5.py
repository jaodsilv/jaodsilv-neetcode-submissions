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


        A = nums1 if len(nums1) < len(nums2) else nums2
        B = nums1 if len(nums1) >= len(nums2) else nums2

        total = len(A) + len(B)
        half = total // 2

        def getPartition(nums, index):
            left = nums[index] if index >= 0 else None
            right = nums[index + 1] if index + 1 < len(nums) else None
            return (left, right)

        def isValidPartition(aLeft, aRight, bLeft, bRight):
            return (aLeft is None or bRight is None or aLeft <= bRight) and (bLeft is None or aRight is None or bLeft <= aRight)

        def maxLeft(a, b):
            if a is None:
                return b
            if b is None:
                return a
            else:
                return max(a, b)
        def minRight(a, b):
            if a is None:
                return b
            if b is None:
                return a
            else:
                return min(a, b)

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2
            aLeft, aRight = getPartition(A, i)
            bLeft, bRight = getPartition(B, j)
            if isValidPartition(aLeft, aRight, bLeft, bRight):
                if total % 2 == 1:
                    return minRight(aRight, bRight)
                else:
                    return (maxLeft(aLeft, bLeft) + minRight(aRight, bRight)) / 2
            elif aLeft and bRight and aLeft > bRight:
                r = i - 1
            else: # bLeft > aRight
                l = i + 1
