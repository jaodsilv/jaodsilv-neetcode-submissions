class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        We have to find an slice on each  array that divides the arrays as follows:
        `nums1[i] <= nums2[j+1] and nums1[i+1] >= nums2[j] and i + j == (m + n) // 2`
        '''
        # With no loss of generality, let's make nums1 the shortest array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m = len(nums1)
        n = len(nums2)

        if m == n == 1:
            return (nums1[0] + nums2[0]) / 2

        is_even = (m + n) % 2 == 0

        # Special cases:
        if m == 0:
            if is_even:
                return (nums2[n // 2] + nums2[n // 2 - 1]) / 2
            else:
                return nums2[n // 2]

        if n == 0:
            if is_even:
                return (nums1[m // 2] + nums1[m // 2 - 1]) / 2
            else:
                return nums1[m // 2]

            
        if nums1[0] >= nums2[-1]:
            j = (m + n) // 2
            if m == n:
                if is_even:
                    return (nums1[0] + nums2[-1]) / 2
                else:
                    return nums1[0]
            if is_even:
                return nums2[j] + nums2[j-1]
            else:
                return nums2[j]
        if nums2[0] >= nums1[-1]:
            j = (m + n) // 2 - m
            if m == n:
                if is_even:
                    return (nums1[-1] + nums2[0]) / 2
                else:
                    return nums2[0]
            if is_even:
                return nums2[j] + nums2[j-1]
            else:
                return nums2[j]

        target = (m + n) // 2
        if m == 1:
            # i is fixed in 0, then, j is also fixed
            l = nums1[0]
            j = target
            if is_even:
                if nums2[j-1] <= l <= nums2[j]:
                    return (max(l, nums2[j-1]) + min(l, nums2[j])) / 2
                else:
                    return (nums2[j-1] + nums2[j]) / 2
            elif nums2[j-1] <= l <= nums2[j]:
                return l
            elif l < nums2[j]:
                return nums2[j]
            else: # elif l > nums2[j]
                return nums2[j-1]
                



        L = 0
        R = m
        while L < R:
            i = (L + R) // 2
            j = target - i
            # nums1[i] <= nums2[j+1] and nums1[i+1] >= nums2[j] and i + j == (m + n) // 2
            if i == 0 or (j < n and nums1[i-1] > nums2[j]):
                R = i
            elif j == 0 or (i < m and nums1[i] < nums2[j-1]):
                L = i+1
            # else we found if
            elif is_even:
              if i == 0:
                return (nums2[j-1] + min(nums1[i], nums2[j])) / 2
              if i == m:
                return (max(nums1[i-1], nums2[j-1]) + nums2[j]) / 2
              elif j == 0:
                return (nums1[i-1] + min(nums1[i], nums2[j])) / 2
              elif j == n:
                return (max(nums1[i-1], nums2[j-1]) + nums1[i]) / 2
              else:
                return (max(nums1[i-1], nums2[j-1]) + min(nums1[i], nums2[j])) / 2
            elif i == m:
                return nums2[j]
            elif j == n:
                return nums1[i]
            else:
                return min(nums1[i], nums2[j])
        print(L, R)

        
