class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        m = max(nums)
        if m <= 0:
            return m
        
        # Let's build a sums array in the following form:
        # We count the biggest sum inclusive, and the biggest sum so far
        # sums = [nums[0]]
        i = 0
        while nums[i] <= 0:
            i += 1
        maxS = nums[i]
        currS = nums[i]
        for j in range(i + 1, len(nums)):
            v = nums[j]
            # sums.append()
            currS = max(0, currS + v)
            maxS = max(maxS, currS)

        return maxS