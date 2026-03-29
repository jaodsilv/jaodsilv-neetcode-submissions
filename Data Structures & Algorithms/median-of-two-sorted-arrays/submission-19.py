import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Force nums1 being the smallest:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        total = len(nums1) + len(nums2)
        mid = total // 2

        def median(arr):
            if len(arr) % 2 == 1:
                return arr[len(arr) // 2]
            else:
                return (arr[(len(arr) // 2) - 1] + arr[len(arr) // 2]) / 2
        # Let's handle spacial cases first
        # 1. nums1 is empty
        if len(nums1) == 0:
            return median(nums2)

        # 2. nums1 is entirely to the left of the median
        # if len(nums1) < len(nums2) and 
        if nums1[-1] <= nums2[mid - len(nums1)]:
            print("test")
            if len(nums1) == len(nums2):
                return median([nums1[-1], nums2[0]])
            elif total % 2 == 1:
                return nums2[mid - len(nums1)]
            else:
                print(f"nums1[-1]: {nums1[-1]}, mid - len(nums1) - 1: {mid - len(nums1) - 1}, nums2[{mid - len(nums1) - 1}]: {nums2[mid - len(nums1) - 1]}, mid - len(nums1): {mid - len(nums1)}, nums2[{mid - len(nums1)}]: {nums2[mid - len(nums1)]}")
                return median([max(nums1[-1], nums2[mid - len(nums1) - 1]),nums2[mid - len(nums1)]])
        # if len(nums1) == len(nums2) and nums1[-1] < nums2[0]:
        #     if total % 2 == 1:

        # 3. nums1 is entirely to the right of the median
        if len(nums1) == len(nums2):
            if nums1[0] >= nums2[-1]:
                return median([nums2[-1], nums1[0]])
        elif nums1[0] >= nums2[mid]:
            if total % 2 == 1:
                return nums2[mid]
            else:
                return median([nums2[mid - 1], min(nums1[0], nums1[mid + 1])])

        def getJ(i):
            return mid - i

        # We have to find partitions where:
        def valid(i) -> int:
            j = getJ(i)
            if i == len(nums1) - 1 or nums1[i] <= nums2[j+1] and nums2[j] <= nums1[i+1]:
                return 0
            if j == len(nums2) - 1 or nums1[i] > nums2[j+1]:
                return 1 # Must move pointer to the right
            return -1

        # If len(nums1) + len(nums2) % 2 == 1:
        # There is a middle element, that said
        # we have to find i partition of the smallest
        L = 0
        R = len(nums1)
        m = R // 2
        v = valid(m)

        count = math.floor(math.log2(R)) + 1
        while count > 0 and v != 0:
            count -= 1
            if v < 0:
                L = m
                m = (R + L) // 2
            else:
                R = m
                m = (R + L) // 2
        print(f'Final R: {R}, L: {L}, mid: {mid}, m: {m}, j: {getJ(m)}')
        m2 = getJ(m)
        if total % 2 == 1:
            return min(nums1[m], nums2[m2])
        else:
            return median([max(nums1[m-1],nums2[m2-1]),min(nums1[m], nums2[m2])])
