import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subnumsLens = [0] * len(nums)
        for i in range(len(nums)):
            maxLen = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    maxLen = max(maxLen, subnumsLens[j] + 1)
            subnumsLens[i] = maxLen
        return max(subnumsLens)
