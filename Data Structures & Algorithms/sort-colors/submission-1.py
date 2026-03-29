class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last0 = -1
        last1 = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                last0 += 1
                nums[last0] = 0
                if last1 >= 0:
                    last1+=1
                    nums[last1] = 1
                if last1 < i and last0 < i:
                    nums[i] = 2
            elif nums[i] == 1:
                if last0 == -1 or last1 >= 0:
                    last1 += 1
                else:
                    last1 = last0 + 1
                nums[last1] = 1
                if last1 < i:
                    nums[i] = 2

