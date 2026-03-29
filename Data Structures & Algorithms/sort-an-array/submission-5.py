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
            i = l
            # print(f'0: p: {p}, L= {L}, R = {R}, l = {l}, r = {r}, nums = {nums}')
            while i <= r:
                # print(f'i: {i}')
                while i < r and nums[i] > p:
                    swap(i, r)
                    r -= 1
                    # print(f'1: p: {p}, L= {L}, R = {R}, l = {l}, r = {r}, nums = {nums}')
                if nums[i] > p:
                    r -= 1
                elif nums[i] < p:
                    if l < i:
                        swap(l, i)
                    l += 1
                    # print(f'2: p: {p}, L= {L}, R = {R}, l = {l}, r = {r}, nums = {nums}')
                # if nums[i] < p:

                i += 1
            if L < l-1:
                unsorted.append((L, l-1))
            if r+1 < R:
                unsorted.append((r+1, R))
            # print(f'3: p: {p}, L= {L}, R = {R}, l = {l}, r = {r}, nums = {nums}, unsorted = {unsorted}')

        # Let's take an average pivot

        return nums