class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            index = nums[i] - 1
            while 0 < nums[i] <= n and nums[i] != nums[index]:
                nums[i], nums[index] = nums[index], nums[i]
                index = nums[i] - 1
            i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1