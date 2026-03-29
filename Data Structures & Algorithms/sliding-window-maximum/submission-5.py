import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        The length of the output is len(nums) - k + 1
        Let's use a max-heap, at each step it adds to the heap the new elements,
        and remove all elements until the top element is whithin the current window position
        '''
        heap = [(nums[i], i) for i in range(k)]
        heapq.heapify_max(heap)
        res = [heap[0][0]]
        for i in range(k, len(nums)):
            heapq.heappush_max(heap, (nums[i], i))
            while heap[0][1] < i - k + 1:
                heapq.heappop_max(heap)
            res.append(heap[0][0])
        return res