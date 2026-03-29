import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def solution1():
            # Let's use a quick sort-like strategy to find the kth element
            # Which is O(n^2) worst case, but average case is O(n)

            def split(arr):
                if len(arr) == 0:
                    return ([],[],[], None)
                def getPivot():
                    a, b, c = arr[0], arr[len(arr)//2], arr[-1]
                    m = min(a, b, c)
                    n = max(a, b, c)
                    if a == n or a == m:
                        if b == n or b == m:
                            return c
                        else:
                            return b
                    else:
                        return a
                L = []
                M = []
                R = []
                pivot = getPivot()
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
        def solution2():
            nums.sort(reverse=True)
            return nums[k-1]

        def solution3():
            heap = []
            for i in nums:
                if len(heap) < k:
                    heapq.heappush(heap, i)
                else:
                    heapq.heappushpop(heap, i)
            return heap[0]
        
        return solution1()