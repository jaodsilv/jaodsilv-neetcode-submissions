class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        if nums[0] == 0:
            return False

        maxRecheable = 0
        for i in range(len(nums)):
            if i > maxRecheable:
                return False
            maxRecheable = max(maxRecheable, i + nums[i])
            if maxRecheable >= len(nums) - 1:
                return True

            