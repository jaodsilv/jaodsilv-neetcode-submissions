import bisect
import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        if m > n:
            m, n = n, m
            nums1, nums2 = nums2, nums1

        if m == 0:
            if n % 2 == 0:
                return (nums2[n // 2] + nums2[(n // 2) - 1]) / 2
            else:
                return nums2[n // 2]

        if n == 0:
            if m % 2 == 0:
                return (nums1[m // 2] + nums1[(m // 2) - 1]) / 2
            else:
                return nums1[m // 2]

        if nums1[-1] <= nums2[0]:
            if m == n:
                return (nums1[-1] + nums2[0]) / 2
            if m > n:
                halfR = ((m + n) // 2)
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

        if nums2[-1] <= nums1[0]:
            if m == n:
                return (nums2[-1] + nums1[0]) / 2
            if n > m:
                halfR = ((m + n) // 2)
                if (m + n) % 2 == 0:
                    return (nums2[halfR - 1] + nums2[halfR]) / 2
                else:
                    return nums2[halfR]

            else:
                halfR = ((m + n) // 2) - n
                if (m + n) % 2 == 0:
                    return (nums1[halfR - 1] + nums1[halfR]) / 2
                else:
                    return nums1[halfR]

        half = (m + n) // 2
        L = 0
        R = m
        pos = (R + L) // 2
        pos2 = half - pos
        
        while True:
            if pos == 0:
                if nums2[pos2 - 1] < min(nums1[pos], nums2[pos2]):
                    break
                else:
                    L = 1
            elif pos == m:
                if max(nums1[pos - 1], nums2[pos2 - 1]) <= nums2[pos2]:
                    break
                else:
                    R = m - 1
            elif max(nums1[pos - 1], nums2[pos2 - 1]) <= min(nums1[pos], nums2[pos2]):
                break
            else:
                if nums1[pos - 1] > nums2[pos2]:
                    R = pos
                else:
                    L = pos + 1
            pos = (R + L) // 2
            pos2 = half - pos

        if (m + n) % 2 == 1:
            if pos >= m:
                return nums2[pos2]
            else:
                return min(nums1[pos], nums2[pos2])
        else:
            if pos >= m:
                return (max(nums2[pos2 - 1], nums1[-1]) + nums2[pos2]) / 2
            elif pos == 0:
                return (nums2[pos2 - 1] + min(nums1[pos], nums2[pos2])) / 2
            else:
                return (max(nums2[pos2-1], nums1[pos-1]) + min(nums1[pos], nums2[pos2])) / 2

