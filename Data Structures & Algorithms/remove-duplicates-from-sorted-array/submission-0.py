class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L, R = 0, 0
        prev = -101
        while R < len(nums):
            nums[L] = nums[R]
            prev = nums[R]
            L += 1
            R += 1
            while R < len(nums) and nums[R] == prev:
                R += 1
        return L