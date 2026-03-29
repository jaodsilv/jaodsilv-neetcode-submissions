class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # O(1) space, O(n) time complexity, but changing nums
        # Once we find a number, we replace it with the number its position
        # Repeate until it points to itself

        for i in range(len(nums)): # i=0; 1
            while nums[i] != i+1: # nums[0]=1; nums[1]=3
                tmp = nums[i] # tmp = 3
                tmp2 = nums[tmp-1] # tmp2 = nums[2] = 4
                if tmp == tmp2: # False
                    return tmp
                nums[tmp-1] = tmp # nums[]
                nums[i] = tmp2
        '''
        # O(n) space, O(n*log(n)) time complexity, and not changing nums
        sNums = sorted(nums)
        for i in range(len(nums) - 1):
            if sNums[i] == sNums[i+1]:
                return sNums[i]
        '''
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