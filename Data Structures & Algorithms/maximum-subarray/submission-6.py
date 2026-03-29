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
        sumsInclusive = [nums[i]]
        for j in range(i + 1, len(nums)):
            v = nums[j]
            # sums.append()
            sInclusive = sumsInclusive[-1] + v
            if sInclusive > 0:
                sumsInclusive.append(sInclusive)
            else:
                sumsInclusive.append(0)

        return max(sumsInclusive)