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

        # Brute force (O(n*k))
        res = []
        for i in range(len(nums)-k+1):
            res.append(max(nums[i:i+k]))
        return res

