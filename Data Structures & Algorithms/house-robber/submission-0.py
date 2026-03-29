class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        # We loop through them looking for the best option among them
        # If we go through all possibilities we will get a O(2**N) time, which is far from ideal
        # We may collect two informations: The maximum sum that may include that house and the maximum sum that does not include the previous house

        somaMax = nums[0]
        somaPre = 0
        for i in range(1, len(nums)):
            cur = somaPre + nums[i]
            somaPre = somaMax
            somaMax = max(somaMax, cur)

        return somaMax