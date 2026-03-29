class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]
        # Let's try to complete that in O(n)
        
        # including 0
        maxInclusiveW0 = nums[0]
        maxNotInclusiveW0 = nums[0]

        # not including 0
        maxInclusive = nums[1]
        maxNotInclusive = 0

        for i in range(2, len(nums) - 1):
            tmp = maxInclusiveW0
            maxInclusiveW0 = max(maxInclusiveW0, maxNotInclusiveW0 + nums[i])
            maxNotInclusiveW0 = max(maxNotInclusiveW0, tmp)
            tmp = maxInclusive
            maxInclusive = max(maxInclusive, maxNotInclusive + nums[i])
            maxNotInclusive = max(maxNotInclusive, tmp)

        tmp = maxInclusive
        maxInclusive = max(maxInclusive, maxNotInclusive + nums[-1])
        maxNotInclusive = max(maxNotInclusive, tmp)
        return max(maxNotInclusiveW0, maxInclusiveW0, maxNotInclusive, maxInclusive)