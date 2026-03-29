class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        # Let's create a prefix sums array (in O(n))
        sums = [nums[0]]
        for i in range(1, len(nums)):
            sums.append(sums[-1] + nums[i])

        '''
        Solutions 1.1: Looping over all possibilities

        # Now we can easily calculate the sums between two points (in O(1)), looping in O(n^2) we can check all sums
        maxSum = max(max(nums), max(sums))
        for i in range(1, len(nums)):
            for j in range(i, len(nums)):
                maxSum = max(maxSum, sums[j] - sums[i-1])
        return maxSum
        
        Done in 6min
        '''

        '''
        Solution 1:
        '''
        maxSums = max(sums)
        index = sums.index(maxSums)
        if index > 0:
            return max(max(nums), maxSums, maxSums - min(sums[:index]))
        else:
            return max(max(nums), maxSums)