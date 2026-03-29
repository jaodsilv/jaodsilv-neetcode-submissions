import heapq
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        # Heap sort
        copy = nums.copy()
        heapq.heapify(copy)
        for i in range(len(nums)):
            nums[i] = heapq.heappop(copy)
        return nums