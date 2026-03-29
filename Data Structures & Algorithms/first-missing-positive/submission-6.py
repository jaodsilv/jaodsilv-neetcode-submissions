import bisect

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Let's first count number of positive elements
        positives = 0
        maxNum = 0
        for i in range(len(nums)):
            if 0 < nums[i] <= len(nums):
                positives += 1
            else:
                nums[i] = 0
            

        # Special Cases:
        if positives == 0:
            return 1

        if positives == 1:
            return 2 if 1 in nums else 1
        print(nums)

        for i in range(positives):
            while 0 < nums[i] != i+1 and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        print(nums)

        for i in range(positives, len(nums)):
            if nums[i] > 0:
                nums[nums[i]-1] = nums[i]

        print(nums)
        for i in range(positives):
            print(f'loop3: i={i}')
            if nums[i] != i+1:
                print(f'test: i+1={i+1} != nums[i]={nums[i]}')
                return i+1

        return positives + 1