class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        def solutionSort(): #O(nlogn)
            nums.sort()
            i = 0
            j = len(nums)
            while j - i > 1:
                m = (i+j)//2
                if nums[m] == m: #Its to the right
                    i = m
                else: #its the target or it is to the left
                    j = m

            m = (i+j)//2
            if nums[m] == m: #Its to the right
                return m + 1
            else:
                return m

        def solutionSet(): # O(n)
            s = set(nums)
            for i in range(len(nums) + 1):
                if i not in s:
                    return i
        # def solutionReplaceInPlace():
        #     while 
        return solutionSet()