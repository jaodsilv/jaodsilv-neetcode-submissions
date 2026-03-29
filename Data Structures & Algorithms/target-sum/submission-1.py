from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # First let`s remove the zeroes, as they do not interfere in the sum and don`t have sign
        # nums = [i for i in nums if i != 0]
        # if len(nums) == 0:
        #     return 0 if target != 0 else 1
        if len(nums) == 1:
            return 0 if abs(target) != nums[0] else 1

        # Let's compact the array
        counter = []
        nums.sort()
        prev = -1
        for i in nums:
            if i != prev:
                counter.append([i, 1])
            else:
                counter[-1][1] += 1
        
        # prefix sum to help us build our dp
        # prefix = []
        # for i, c in counter:
        #     prefix.append(c*i)

        memo = {}
        visited = set()

        def dfs(i, curr):
            pair = (i, curr)
            if pair in memo:
                return memo[pair]
            
            if i == len(counter):
                return 1 if curr == target else 0
            v, c = counter[i]
            # Values can go from -v*c to v*c with a step of 2*v
            # Which means we can have (c + 1) different sums
            curr = curr - v*c
            step = 2*v
            possibilities = 0
            for j in range(c+1):
                # j representing the number of positive numbers v
                possibilities += dfs(i+1, curr)*math.comb(c, j)
                curr += step
            memo[pair] = possibilities
            return possibilities
        return dfs(0, 0)
        # To make things easier we can shift everything
        