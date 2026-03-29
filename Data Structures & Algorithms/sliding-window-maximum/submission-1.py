import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        1,2,1,0,4,2,6

        Max left to right:
        1,2,2,2,4,4,6
        Max right to left:
        6,6,6,6,6,6,6
        
        '''
        if k == 1:
            return nums
        if k == len(nums):
            return [max(nums)]

        res = []
        nums = [(num, i) for i, num in enumerate(nums)]
        print(nums)
        heap = nums[:k-1]
        print(heap)
        heapq.heapify_max(heap)
        print(heap)
        for i in range(len(nums)-k+1):
            heapq.heappush_max(heap, nums[i+k-1])
            top = heap[0]
            while top[1] < i:
                heapq.heappop_max(heap)
                top = heap[0]
            res.append(top[0])
            print(heap)
        return res

            
        