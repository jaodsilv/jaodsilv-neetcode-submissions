class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def medianSingleArray(arr):
            if len(arr) == 0:
                return 0
            mid = len(arr) // 2
            if len(arr) % 2 == 0:
                return (arr[mid-1] + arr[mid]) / 2
            else:
                return arr[mid]

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

        return solutionBruteForce()
        