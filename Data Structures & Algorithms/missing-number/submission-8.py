class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = len(nums)
        for i in range(len(nums)):
            total += i - nums[i]
        return total