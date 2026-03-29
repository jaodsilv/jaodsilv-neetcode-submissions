class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # O(n) space, O(n*log(n)) time complexity, and not changing nums
        sNums = sorted(nums)
        for i in range(len(nums) - 1):
            if sNums[i] == sNums[i+1]:
                return sNums[i]
        '''
        # O(1) space, O(n*log(n)) time complexity, but changing nums
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return nums[i]
        '''
        '''
        # O(n) space, O(n) time complexity
        found = [False]*len(nums)
        for i in nums:
            if found[i]:
                return i
            found[i] = True
        '''