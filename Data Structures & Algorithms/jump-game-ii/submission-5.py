class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        # This problem can be rewritten as instervals where we want the minimum number of intervals where:
        # - all points are covered
        # - each interval starts at i
        jumps = 0
        i = 0
        nextReach = 0
        while nextReach < n - 1:
            jumps += 1
            reach = nextReach
            while i <= reach:
                nextReach = max(nextReach, i + nums[i])
                i += 1
        return jumps
        # The last position value is not relevant