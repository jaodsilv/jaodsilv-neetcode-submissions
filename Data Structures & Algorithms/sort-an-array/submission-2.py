class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        # To minimize space complexity it would be ideal to be a iterative, not recursive solution, and in-place
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        def pivot(L, R):
            l, m, r = nums[L], nums[(L+R)//2], nums[R]
            return l+m+r-min(l, m, r)-max(l, m, r)

        # Quick sort: O(nlogn) time in average
        unsorted = [(0, len(nums)-1)]
        while unsorted:
            L, R = unsorted.pop()
            l, r = L, R
            p = pivot(l,r)
            for i in range(r+1):
                while r > l and nums[i] > p:
                    swap(i, r)
                    r -= 1
                if nums[i] < p and l < i:
                    swap(l, i)
                    l += 1
            if l > L:
                unsorted.append((L, l))
            if r < R:
                unsorted.append((r+1, R))

        # Let's take an average pivot

        return nums