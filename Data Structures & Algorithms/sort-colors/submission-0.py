class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count0 = 0
        count1 = 0
        count2 = 0
        for n in nums:
            if n == 0:
                count0 += 1
            elif n == 1:
                count1 += 1
            else:
                count2 += 1
        for i in range(len(nums)):
            if count0:
                nums[i] = 0
                count0 -= 1
            elif count1:
                nums[i] = 1
                count1 -= 1
            else: # elif count2:
                nums[i] = 2

