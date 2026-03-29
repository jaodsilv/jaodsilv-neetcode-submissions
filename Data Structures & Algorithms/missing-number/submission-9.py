class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        def solutionMath():
            total = len(nums)
            for i in range(len(nums)):
                total += i - nums[i]
            return total

        def solutionXor():
            res = len(nums)
            for i in range(len(nums)):
                res ^= i ^ nums[i]
            return res

        return solutionXor()