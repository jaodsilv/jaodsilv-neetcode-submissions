class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Brute Force
        for i in range(1, len(nums)):
            found = False
            for j in nums:
                if j == i:
                    if found:
                        return j
                    else:
                        found = True
