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

        def solutionReplaceInPlace():
            n = len(nums)
            i = 0
            while i < n:
                while nums[i] != i:
                    if nums[i] == n:
                        break
                    tmp = nums[nums[i]]
                    nums[nums[i]] = nums[i]
                    nums[i] = tmp
                i += 1
            for i, num in enumerate(nums):
                if i != num:
                    return i
            return n

        def solutionXor():
            n = len(nums)
            res = n
            for i in range(n):
                res ^= i ^ nums[i]
            return res
        return solutionXor()