class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        Solution 1:
        '''
        '''
        numsSet = set(nums)
        return len(numsSet) != len(nums)

        Solution 2:
        '''

        numsSet = set()
        for i in nums:
            if i in numsSet:
                return True
            numsSet.add(i)
        return False