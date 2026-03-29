class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # O(n) space, O(n) time complexity
        found = [False]*len(nums)
        for i in nums:
            if found[i]:
                return i
            found[i] = True