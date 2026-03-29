from collections import deque
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        # Quick Sort
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        def pivot(L, R):
            return (nums[L] + nums[(L+R)//2] + nums[R]) // 3

        def sort(L, R):
            p = pivot(L, R)
            i, l, r = L, L, R
            while i <= r:
                n = nums[i]
                if n > p:
                    swap(i, r)
                    r -= 1
                elif n == p:
                    i += 1
                else:# elif n < p:
                    if l < i:
                        swap(i,l)
                    l += 1
                    i += 1
            for j in range(l, r+1):
                nums[j] = p
            
            return (l-1, r+1)

        unsorted = [(0, len(nums)-1)]
        while unsorted:
            L, R = unsorted.pop()
            l, r = sort(L, R)
            if L < l:
                unsorted.append((L, l))
            if R > r:
                unsorted.append((r, R))
        return nums