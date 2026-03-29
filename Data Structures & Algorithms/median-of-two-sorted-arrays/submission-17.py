import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def medianSingleArray(arr):
            if len(arr) == 0:
                return 0
            mid = (len(arr) - 1) // 2
            if len(arr) % 2 == 0:
                return (arr[mid] + arr[mid + 1]) / 2
            else:
                return arr[mid]

        if len(nums1) == 0:
            return medianSingleArray(nums2)

        if len(nums2) == 0:
            return medianSingleArray(nums1)

        def solutionBruteForce(): # O(nlogn)
            nums1.extend(nums2)
            nums1.sort()
            print(nums1)
            return medianSingleArray(nums1)

        def solutionMerge(): # O(n)
            nums = []
            i = j = 0
            while i < len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    nums.append(nums1[i])
                    i += 1
                else:
                    nums.append(nums2[j])
                    j += 1
            if i < len(nums1):
                nums.extend(nums1[i:])
            else:
                nums.extend(nums2[j:])
            return medianSingleArray(nums)

        def solutionSliceBinarySearch():
            '''
            We have to find i and j that divides
            nums1 and nums2 respectively so 
            i + j = (m + n - 1) // 2
            and nums1[i] <= nums2[j + 1] and nums2[j] <= nums1[i + 1]
            '''
            m = len(nums1)
            n = len(nums2)



            if m <= n:
                shorter = nums1
                longer = nums2
            else:
                m, n = n, m
                shorter = nums2
                longer = nums1
            
            target = (m + n + 1) // 2 # meaning number of elements in the left + middle if odd, not an index
            # if (m+n) % 2 == 0:
            #     target -= 1

            # Test if shorter is entirely to the right of the meadian
            print('target:', target)
            medianPos = target - 1 # This is an index
            print(f'medianPos = {medianPos}')
            if medianPos <= n and longer[medianPos] <= shorter[0]:
                if (m + n) % 2 == 1:
                    return longer[medianPos]
                else:
                    if medianPos == n - 1:
                        return (longer[medianPos] + shorter[0]) / 2
                    else:
                        return (longer[medianPos] + min(shorter[0], longer[medianPos + 1])) / 2

            # Test if the shorter is entirely at the left of the median
            medianPos = target - m # This the index of the first of the right slice

            print(f'medianPos = {medianPos}')
            if longer[medianPos] >= shorter[-1]:
                if (m + n) % 2 == 1:
                    return max(shorter[-1], longer[medianPos - 1])
                else:
                    if medianPos == 0:
                        return (shorter[-1] + longer[medianPos]) / 2
                    else:
                        return (max(shorter[-1], longer[medianPos - 1]) + longer[medianPos]) / 2

            # Case 1: Even number of elements
            # i + j + 2 = target
            left = 0
            right = m

            i = min(max(0, (m // 2) - 1), m - 1) # index of last element of the left slice
            j = min(max(0, target - i - 2), m - 1) # index of last element of the left slice
            print(left, right, i, j, target)
            count = 12 # Should be enough to cover all cases if it is correct
            while count and (right > left and ((j < n - 1 and shorter[i] > longer[j + 1]) or (i < m -1 and shorter[i + 1] < longer[j]))):
                count -= 1
                if j < n - 1 and shorter[i] > longer[j + 1]:
                    print("1: i + 1 = ", i + 1, j, shorter[i], longer[j + 1])
                    right = i
                if i < m - 1 and shorter[i + 1] < longer[j]:
                    print('2:', i, "j + 1 =", j + 1, shorter[i + 1], longer[j])
                    left = i
                i = min(max(0, ((left + right) // 2)), m - 1)
                j = min(max(0, target - i - 2), n - 1)
            print('0:', i, j, m + n)
            if (m + n) % 2 == 1:
                if i == m:
                    return longer[j]
                if j == n:
                    return shorter[i]
                return max(shorter[i], longer[j])
            else:
                if i == m - 1:
                    return (max(shorter[i], longer[j]) + longer[j + 1]) / 2
                elif j == n - 1:
                    return (max(shorter[i], longer[j]) + shorter[i + 1]) / 2
                else:
                    return (max(shorter[i], longer[j]) + min(shorter[i + 1], longer[j + 1])) / 2


        return solutionSliceBinarySearch()
        