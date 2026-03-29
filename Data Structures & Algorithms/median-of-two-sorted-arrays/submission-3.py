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

        # Brute force solution
        merged = sorted(nums1 + nums2)
        return median(merged)
        '''
        Properties of the median
        It is the middle element of the array
        for a single array it is always in the position n // 2 for even arrays or the average between the positions n//2 and n//2+1
        If I merge two arrays

        Consider array a1 and a2 with medians m1 and m2
        We need to find who is(are) the element(s) in the middle of the merged array.
        i.e., we have to find the element which has the same number of elements to the left and to the right
        Let's say, with no loss of generality, that it is the ith element of a1 (0 based) and it's insertion point in a2 is j
        it means it has i elements in a1 to the left and len(a1) - i - 1 elements to the right
        and it would have j elements before it in a2 and len(a2) - j elements to the right
        if they are even sized elements we have 2 medians, n//2 would hit in the right side.
        We know also that (len(a1) + len(a2)) // 2 = i + j


        If find the insertion position of the median of one array in the other array I can know how many elements there will be to the left 
        '''
        if len(nums1) == 0 and len(nums2) == 0:
            return 0

        def approveCandidate(c1, c2, target):
            return c1 + c2 - target
        if len(nums1) == 0:
            return median(nums2)
        if len(nums2) == 0:
            return median(nums1)
        if nums1[0] >= nums2[-1]:
            if len(nums1) > len(nums2):
                return median(nums1[:-len(nums2)])
            elif len(nums1) < len(nums2):
                return median(nums2[len(nums1):])
            else:
                return (nums1[0] + nums2[-1]) / 2
        if nums2[0] >= nums1[-1]:
            if len(nums1) > len(nums2):
                return median(nums1[len(nums2):])
            elif len(nums1) < len(nums2):
                return median(nums2[:-len(nums1)])
            else:
                return (nums1[-1] + nums2[0]) / 2

        m1 = median(nums1) # 1.5
        m2 = median(nums2) # 2.0
        # We can know for sure that the median must be between min(m1, m2) and max(m1, m2), inclusive if they are equal
        l1, l2 = 0, 0

        r1, r2 = len(nums1), len(nums2)
        target = len(nums1) + len(nums2)
        isOdd = target % 2 == 1
        target //= 2
        if not isOdd:
            target -= 1
        print(target)
        while l1 < r1 and l2 < r2:
            candidate = (m1 + m2) // 2
            c1 = bisect.bisect_left(nums1, candidate, l1, r1)
            c2 = bisect.bisect_left(nums2, candidate, l2, r2)
            print(l1, r1, l2, r2, m1, m2, candidate, c1, c2)
            if approveCandidate(c1, c2, target) == 0:
                if isOdd:
                    if candidate == nums1[c1] or candidate == nums2[c2]:
                        return candidate
                    else:
                        return min(nums1[c1], nums2[c2])
                else:
                    candidate2 = 0
                    if nums1[c1] == candidate:

                        candidate2 = min(nums2[c2], nums1[c1+1])
                    else:
                        candidate2 = min(nums2[c2 + 1], nums1[c1])
                    return (candidate + candidate2) / 2
            if m1 < m2: # True
                l1 = bisect.bisect_left(nums1, m1, l1, r1) # 1
                l2 = c2
                r1 = c1
                r2 = bisect.bisect_left(nums2, m2, l2, r2)
            else:
                r1 = bisect.bisect_left(nums1, m1, l1, r1)
                r2 = c2
                l1 = c1
                l2 = bisect.bisect_left(nums2, m2, l2, r2)
            m1 = median(nums1[l1:r1])
            m2 = median(nums1[l2:r2])
        print(m1, m2, candidate)
        diff = approveCandidate(c1, c2, target)
        while not diff != 0:
            if diff > 0:
                if isOdd:
                    candidate -= 1
                else:
                    candidate -= 0.5
            else:
                if isOdd:
                    candidate += 1
                else:
                    candidate += 0.5
            c1 = bisect.bisect_left(nums1, candidate, l1, r1)
            c2 = bisect.bisect_left(nums2, candidate, l2, r2)

        if isOdd:
            if candidate == nums1[c1] or candidate == nums2[c2]:
                return candidate
            else:
                return min(nums1[c1], nums2[c2])
        else:
                candidate2 = 0
                if nums1[c1] == candidate:
                    candidate2 = min(nums2[c2], nums1[c1+1])
                else:
                    candidate2 = min(nums2[c2 + 1], nums1[c1])
                return (candidate + candidate2) / 2

        return candidate
