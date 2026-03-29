from collections import deque
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        # Merge sort
        def merge(l, r):
            if l == r:
                return
            if l == r - 1:
                nums[l], nums[l+1] = min(nums[l:r+1]), max(nums[l:r+1])
            m = (l+r) // 2
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

        def sort(l, r):
            if l == r:
                return
            m = (l+r) // 2
            sort(l, m)
            sort(m+1, r)
            merge(l, r)

        sort(0, len(nums)-1)
        return nums