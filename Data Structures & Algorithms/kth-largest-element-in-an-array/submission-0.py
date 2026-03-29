class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Let's use a quick sort-like strategy to find the kth element
        def split(arr):
            if len(arr) == 0:
                return ([],[],[], None)

            L = []
            M = []
            R = []
            pivot = arr[0]
            for i in arr:
                if i < pivot:
                    L.append(i)
                elif i > pivot:
                    R.append(i)
                else:
                    M.append(i)

            return (L, M, R, pivot)
        
        right = 0
        L, M, R, pivot = split(nums)
        while right != k:
            if right + len(R) < k: # kth largest element is either in M or L
                right += len(R)
                if right + len(M) >= k: # kth largest element is in M, whose size is >= 1
                    return pivot
                else: # if right + len(M) < k, kth largest element is either in L
                    right += len(M)
                    L, M, R, pivot = split(L)
            else: # if right + len(R) >= k, kth largest element is in R
                L, M, R, pivot = split(R)

        return pivot