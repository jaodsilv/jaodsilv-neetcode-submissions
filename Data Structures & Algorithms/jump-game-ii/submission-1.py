class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        for i in range(len(nums) - 2, -1, -1):
            jump = nums[i]
            if jump == 0:
                dp[i] = len(nums)
            else:
                dp[i] = min(dp[i+1:min(i + jump + 1, len(nums))]) + 1
        return dp[0]