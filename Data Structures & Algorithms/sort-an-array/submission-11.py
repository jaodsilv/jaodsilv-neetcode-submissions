import heapq
from collections import deque
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        # Merge sort
        def merge(l, m, r):
            if l == r:
                return
            if l == r - 1:
                nums[l], nums[l+1] = min(nums[l:r+1]), max(nums[l:r+1])
                return
            i, j = l, m+1
            tmp = []
            while i <= m and j <= r:
                val = min(nums[i], nums[j])
                tmp.append(val)
                if val == nums[i]:
                    nums[i] = tmp[i-l]
                    i += 1
                else:
                    j += 1
            tmp.extend(nums[i:m+1] + nums[j:r+1])
            for k in range(i, r+1):
                nums[k] = tmp[k-l]

        level = 1
        while level < len(nums):
            for i in range(0, len(nums), 2*level):
                print(f'merge: nums[{i}:{i+level}] with nums[{i+level}:{min(len(nums)-1,i+2*level)}]')
                merge(i, i+level-1, min(i + 2*level - 1, len(nums)-1))
            level <<= 1
        return nums