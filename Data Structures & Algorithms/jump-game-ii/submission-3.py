class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        # This problem can be rewritten as instervals where we want the minimum number of intervals where:
        # - all points are covered
        # - each interval starts at i
        maxReach = []
        reverseMap = {}
        lastReach = -1
        for i, num in enumerate(nums):
            reach = min(num + i, n-1)
            maxReach.append(reach)
            if reach <= lastReach:
                continue
            for j in range(lastReach + 1, reach + 1):
                reverseMap[j] = i
            lastReach = reach
        i = n-1
        jumps = 0
        while i > 0:
            i = reverseMap[i]
            jumps += 1
        return jumps
        # The last position value is not relevant