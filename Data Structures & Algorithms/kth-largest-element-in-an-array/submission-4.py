class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k == 1:
            return max(nums)
        if k == len(nums):
            return min(nums)

        # Let's do it with a quick selection strategy

        def selectPivot(arr):
            return sorted([arr[0], arr[len(arr)//2], arr[-1]])[1]
        def select(arr):
            pivot = selectPivot(arr)

            L, M, R = [], [], []
            for n in arr:
                if n < pivot:
                    L.append(n)
                elif n > pivot:
                    R.append(n)
                else: # n== pivot
                    M.append(n)
            return L, M, R

        L, M, R = select(nums)
        if len(R) >= k:
            return self.findKthLargest(R, k)
        elif len(R) + len(M) >= k:
            return selectPivot(nums)
        else: # Kth biggest number is in L
            return self.findKthLargest(L, k-len(M)-len(R))
