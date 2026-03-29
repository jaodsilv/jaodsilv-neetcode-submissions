class Solution:
    def jump(self, nums: List[int]) -> int:
        def solutionDP():
            dp = [0]*len(nums)
            for i in range(len(nums) - 2, -1, -1):
                jump = nums[i]
                if jump == 0:
                    dp[i] = len(nums)
                else:
                    dp[i] = min(dp[i+1:min(i + jump + 1, len(nums))]) + 1
            return dp[0]
        def solutionGreedy():
            l = r = jumps = 0
            while r < len(nums) - 1:
                jumps += 1
                nextL = l
                nextR = r
                for i in range(l, r + 1):
                    if i + nums[i] > nextR:
                        nextR = i + nums[i]
                        nextL = i
                l = nextL
                r = nextR
            return jumps
        # return solutionDP()
        return solutionGreedy()