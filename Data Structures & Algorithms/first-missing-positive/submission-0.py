import bisect

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Let's first count number of positive elements
        positives = 0
        maxNum = 0
        for n in nums:
            if n > 0:
                positives += 1
        for n in nums:
            if n > positives + 1:
                positives -= 1
        # Now we count the number of positive elements that are greater than positives + 1
        # Consider the elements from 1 to positives + 1
        # We can be sure the element we want is between this range
        # We must find it without storing an array and without sorting
        
        # Brute Force (O(n²) time, O(1) space)
        # for i in range(1, positives + 2):
        #     if i not in nums:
        #         return i

        # Sorting O(nlogn) time and O(1) extra space for sorting in-place
        nums.sort()
        initial_index = bisect.bisect_left(nums, 1)
        prevVal = 0
        for i in range(initial_index, len(nums)):
            if nums[i] > prevVal + 1:
                return prevVal + 1
            if nums[i] == prevVal + 1:
                prevVal = nums[i]
        
        return prevVal + 1
