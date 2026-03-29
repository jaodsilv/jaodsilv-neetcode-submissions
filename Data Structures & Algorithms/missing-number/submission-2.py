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
        # Lets use a quick selection algorithm, which run in O(n) in average.
        # The goal is to find the element that has 2 elements

        def pivot(arr, i, j):
            a,b,c = arr[i], arr[(i + j) // 2], arr[j]
            m = max(a,b, c)
            n = min(a, b, c)
            if m == a:
                if n == b:
                    return c
                else:
                    return b
            if m == b:
                if n == a:
                    return c
                else:
                    return a
            if n == a:
                return b
            else:
                return a
        # def select():
            # i = 0, j = max
        
        return solutionSort()