import heapq
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        # Count sort
        ## Map values
        objMap = {}
        freqs = []
        for i in range(len(nums)):
            n = nums[i]
            if n not in objMap:
                obj = [n, 1]
                objMap[n] = obj
                heapq.heappush(freqs, obj)
            else:
                objMap[n][1] += 1
        j = 0
        n = 0
        for i in range(len(nums)):
            if j == 0:
                n, j = heapq.heappop(freqs)
            nums[i] = n
            j -= 1
        return nums


