from collections import deque
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        # Quick Sort
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        def pivot(L, R):
            l, m, r = nums[L], nums[(L+R)//2], nums[R]
            return (l+m+r) // 3

        def sort(L, R):
            if L >= R:
                return
            p = pivot(L, R)
            tmp = [0]*(R-L+1)
            l, r = 0, R-L
            for n in nums[L:R+1]:
                if n > p:
                    tmp[r] = n
                    r -= 1
                elif n < p:
                    tmp[l] = n
                    l += 1
            r += 1
            for i in range(l):
                nums[i+L] = tmp[i]
            sort(L, L+l-1)
            for i in range(l, r):
                nums[i+L] = p
            for i in range(r, len(tmp)):
                nums[i+L] = tmp[i]
            sort(L+r, R)


        sort(0, len(nums)-1)
        return nums