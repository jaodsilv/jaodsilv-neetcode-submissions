import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        Solution 1
        subnumsLens = [0] * len(nums)
        for i in range(len(nums)):
            maxLen = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    maxLen = max(maxLen, subnumsLens[j] + 1)
            subnumsLens[i] = maxLen
        return max(subnumsLens)
        '''

        '''
        Solution 2
        '''
        dp = []
        dp.append(nums[0])

        maxLen = 1
        for i in range(1, len(nums)):
            # If it is larger than the lat in the dp we append it to the end
            if dp[-1] < nums[i]:
                dp.append(nums[i])
                maxLen += 1
                continue
            
            # Otherwise we update the position where it would fit.
            # This works because it will only reach the dp[-1] if we have enough entries in this new sequence.
            # Working like a branching of th sequence, but without the extra space.
            idx = bisect.bisect_left(dp, nums[i])
            dp[idx] = nums[i]

        return maxLen