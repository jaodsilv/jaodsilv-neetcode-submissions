import bisect
import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Since our goal is O(log(m + n)) time we must use binary search to find the median
        # Let`s start checking the edge cases:
        m = len(nums1)
        n = len(nums2)

        if m > n:
            m, n = n, m
            nums1, nums2 = nums2, nums1

        # m == 0
        if m == 0:
            if n % 2 == 0:
                return (nums2[n // 2] + nums2[(n // 2) - 1]) / 2
            else:
                return nums2[n // 2]

        # n == 0
        if n == 0:
            if m % 2 == 0:
                return (nums1[m // 2] + nums1[(m // 2) - 1]) / 2
            else:
                return nums1[m // 2]

        # nums1[-1] <= nums2[0]
        if nums1[-1] <= nums2[0]:
            if m == n:
                return (nums1[-1] + nums2[0]) / 2
            if m > n:
                halfR = ((m + n) // 2)
                print(halfR)
                if (m + n) % 2 == 0:
                    return (nums1[halfR - 1] + nums1[halfR]) / 2
                else:
                    return nums1[halfR]

            else: # m < n:
                halfR = ((m + n) // 2) - m
                if (m + n) % 2 == 0:
                    return (nums2[halfR - 1] + nums2[halfR]) / 2
                else:
                    return nums2[halfR]

        # nums1[0] >= nums2[-1]
        if nums2[-1] <= nums1[0]:
            if m == n:
                return (nums2[-1] + nums1[0]) / 2
            if n > m:
                halfR = ((m + n) // 2)
                print(halfR)
                if (m + n) % 2 == 0:
                    return (nums2[halfR - 1] + nums2[halfR]) / 2
                else:
                    return nums2[halfR]

            else: # m < n:
                halfR = ((m + n) // 2) - n
                if (m + n) % 2 == 0:
                    return (nums1[halfR - 1] + nums1[halfR]) / 2
                else:
                    return nums1[halfR]

        # Generalizing the two cases above to when median is greater than or smaller than all items from the other array
        # Lets find the insertion points of nums1[0]
        # if m > n:

        # else:


        # The goal is to find the element that would be the element (n+m) // 2 of the merged array, but without merging it
        # This is the same as finding x, and y, such as the insertion point of nums1[x] in nums2 is y, and vice-versa, while x+y = (m + n) // 2
        half = (m + n) // 2
        L = 0
        R = m
        pos = (R + L) // 2
        pos2 = half - pos
        
        # If m+n % 2 == 1
        # the found partition will be x + y = (m + n) / 2 - 1, which should give us the  
        
        while True:
            # print(L, R, pos, pos2)
            # Left Partitions nums1[:pos] and nums2[:pos2]
            # Right Partitions nums1[pos:] and nums2[pos2:]
            if pos == 0: # Left nums1 is empty
                if nums2[pos2 - 1] < min(nums1[pos], nums2[pos2]):
                    # valid
                    break
                else:
                    # invalid
                    L = 1
            elif pos == m: # Right nums1 is empty
                if max(nums1[pos - 1], nums2[pos2 - 1]) <= nums2[pos2]:
                    # valid
                    break
                else:
                    # invalid
                    R = m - 1
            elif max(nums1[pos - 1], nums2[pos2 - 1]) <= min(nums1[pos], nums2[pos2]):
                # valid
                break
            else:
                # invalid
                if nums1[pos - 1] > nums2[pos2]:
                    R = pos
                else:
                    L = pos + 1
                # R = pos
                # R2 = pos2
                # L2 = 0
            # else:
                # L = pos
                # L2 = pos2
                # R2 = n
            pos = (R + L) // 2
            pos2 = half - pos
            # prev = pos
            # prev2 = pos2
            # pos = (R + L) // 2
            # pos2 = bisect.bisect_left(nums2, nums1[pos])#, lo=L2, hi=R2)

        # if pos + pos2 == half - 1:
        #     # we get the min of the next elements
        #     if pos == m - 1 and pos2 == n - 1:
        #     if pos == m - 1 and pos2 < n - 1:
        #         return nums2[pos2 + 1]
        #     elif pos2 == n - 1 and pos < m - 1:
        #         return nums1[pos + 1]
        #     else:

        print(L, R, pos, pos2)

            
        # We 2 great candidates, nums1[pos] and nums2[pos2]

        if (m + n) % 2 == 1:
            # Choose the min of nums1[pos] and nums2[pos2]
            if pos >= m:
                return nums2[pos2]
            else:
                return min(nums1[pos], nums2[pos2])
        else: # if (m + n) % 2 == 0:
            # We should pick the average of the max of the left and the min of the right
            # Here we have to find if the median is nums1[pos] or nums2[pos2]
            if pos >= m:
                return (max(nums2[pos2 - 1], nums1[-1]) + nums2[pos2]) / 2
            elif pos == 0:
                return (nums2[pos2 - 1] + min(nums1[pos], nums2[pos2])) / 2
            else:
                return (max(nums2[pos2-1], nums1[pos-1]) + min(nums1[pos], nums2[pos2])) / 2

