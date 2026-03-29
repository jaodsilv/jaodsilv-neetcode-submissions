class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # a ^ a = 0
        # a ^ 0 = a
        single = 0
        for num in nums:
            single ^= num
        return single