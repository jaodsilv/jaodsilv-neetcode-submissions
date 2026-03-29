from collections import defaultdict

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # nummap = defaultdict(list)
        # for i, num in enumerate(nums):
        #     nummap[num].append(i)
        # values = sorted(nummap.keys())
        '''
            lists where the we get smallest last elements
            Each possible increasing subsequencce can be represented by a two numbers at any step.
            subsequence = (lastNumber, length)
            at each number we increase the length of all subsequences we can
            1. At any point, if there are 2 subsequences such as (x1, l) and (x2, l) where x1 <= x2, we can safely drop (x2, l)
            2. At any point, if there are 2 subsequences such as (x, l1) and (x, l2) where l1 >= l2, we can safely drop (x, l2)
            3. At any point, if there are 2 subsequences such as (x1, l1) and (x2, l2) where x1 <= x2 AND l1 >= l2, we can safely drop (x2, l2)
            3. At any point, if there are 2 subsequences such as (x1, l1) and (x2, l2) where x1 - 1 == x2 AND l1 > l2, we can safely drop (x2, l2)
            To keep them sorted we may use a heap and a map, the heap so we can get the smallest available sequence.
            We start with single element queue with the first num
            we add the next, if it greater than the previous
        '''
        # Compute the longest increasing subsequence starting from i, where 
        # def dfs(i, nummap):
        #     nums[i]

        # Brute force
        topVal = max(nums) + 1
        memo = {}
        def dfs(i) -> int:
            if i == len(nums) - 1:
                return 1
            if i in memo:
                return memo[i]
            val = nums[i]
            maxSub = 1
            minFound = topVal
            for j in range(i+1, len(nums)):
                if nums[j] < minFound and nums[j] > val:
                    minFound = nums[j]
                    maxSub = max(maxSub, dfs(j) + 1)
            memo[i] = maxSub
            print(memo)
            return maxSub
        minFound = topVal
        maxSub = 0
        for j in range(len(nums)):
            if nums[j] >= minFound:
                continue
            minFound = nums[j]
            maxSub = max(maxSub, dfs(j))
        return maxSub