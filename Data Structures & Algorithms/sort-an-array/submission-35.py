from collections import deque
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Shell Sort
        n = len(nums)
        if n == 1:
            return nums
        gap = n // 2
        while gap >= 1:
            for i in range(gap, n):
                tmp = nums[i]
                j = i - gap
                while j >= 0 and nums[j] > tmp:
                    nums[j + gap] = nums[j]
                    j -= gap
                nums[j + gap] = tmp
            gap //= 2
        return nums
    def sortArray_mergesort(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        # Merge sort
        def merge(l, m, r):
            '''
            merge the ranges from l to m and from m+1 to r, inclusive
            '''
            if l == r:
                return
            if l == r - 1:
                nums[l], nums[l+1] = min(nums[l:r+1]), max(nums[l:r+1])
                return
            
            tmp = deque(nums[l:m+1] + nums[m+1:r+1][::-1])
            for i in range(l, r+1):
                if tmp[0] < tmp[-1]:
                    nums[i] = tmp.popleft()
                else:
                    nums[i] = tmp.pop()
    
        level = 1
        while level < len(nums):
            for i in range(0, len(nums), 2*level):
                print(f'merge: nums[{i}:{i+level}] with nums[{i+level}:{min(len(nums)-1,i+2*level)}]')
                merge(i, i+level-1, min(i + 2*level - 1, len(nums)-1))
            level <<= 1
        return nums