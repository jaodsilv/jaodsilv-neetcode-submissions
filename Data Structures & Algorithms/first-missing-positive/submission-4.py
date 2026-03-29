import bisect

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Let's first count number of positive elements
        positives = 0
        maxNum = 0
        for n in nums:
            if n > 0:
                positives += 1

        if positives == 0:
            return 1

        if positives == 1:
            return 2 if 1 in nums else 1
        # This is not really neeeded, but it would save some time
        # Now we count the number of positive elements that are greater than positives + 1
        belowMax = positives + 1 if positives < len(nums) else positives
        for n in nums:
            if n > belowMax:
                belowMax -= 1

        # Consider the elements from 1 to positives + 1
        # We can be sure the element we want is between this range
        # We must find it without storing an array a set or anything like that and without sorting so we get O(n) time and O(1) space
        print(belowMax)
        belowMax = min(belowMax+1, len(nums))
        for i in range(belowMax):
            print(f'loop1: i={i}')

            # We swap it until we get either the ideal number or one that is out of the range.
            # Worst case would be O(n), but it would only happen once in the entire loop case.
            # i.e., the for looop above is actually O(n), not O(n²), with n = belowMax + 2
            while nums[i] != i+1 and 0 < nums[i] < belowMax and nums[nums[i]-1] != nums[i]:
                print(f'swap11: nums[i]={nums[i]}, nums[nums[i]-1]={nums[nums[i]-1]}')
                tmp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = tmp

        for i in range(belowMax, len(nums)):
            print(f'loop2: i={i}')
            if 0 < nums[i] < belowMax:
                print(f'swap2: nums[i]={nums[i]}, nums[nums[i]-1]={nums[nums[i]-1]}')
                # We don't care about losing the values out of our range of search
                nums[nums[i]-1] = nums[i]

        # Special Case:
        print(nums)
        for i in range(belowMax):
            print(f'loop3: i={i}')
            if nums[i] != i+1:
                print(f'test: i+1={i+1} != nums[i]={nums[i]}')
                return i+1

        return belowMax + 1
        # Maximum value of nums[i] is int.MaxValue, therefore we cannot sum them all
        # If we xor them against their range we would get multiple holes, and what about the repeated items


        # Brute Force (O(n²) time, O(1) space)
        # for i in range(1, positives + 2):
        #     if i not in nums:
        #         return i

        # Sorting O(nlogn) time and O(1) extra space for sorting in-place
        # nums.sort()
        # initial_index = bisect.bisect_left(nums, 1)
        # prevVal = 0
        # for i in range(initial_index, len(nums)):
        #     if nums[i] > prevVal + 1:
        #         return prevVal + 1
        #     if nums[i] == prevVal + 1:
        #         prevVal = nums[i]
        
        # return prevVal + 1
