class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Especial cases:
        if len(nums) == 1:
            return False

        total = sum(nums)
        if total % 2 == 1: # cannot be divided in 2
            return False

        # We have to find 1 subset which sum is total // 2
        target = total // 2

        def solutionRecursionOptmized():
            # Nums[i] are limited to be between 1 and 50, let's compute a counter array
            counter = [0]*51
            for n in nums:
                counter[n] += 1

            # Now we can perform a backtrack to find if there is such subset
            def backtrack(i, curr):
                if curr == target:
                    return True
                if i > 50 or curr + i > target:
                    return False
                if backtrack(i + 1, curr):
                    return True
                for k in range(counter[i]):
                    curr += i
                    if curr > target:
                        return False
                    if backtrack(i + 1, curr):
                        return True
                return False

            return backtrack(1, 0)

        def solutionDPTopDown():
            memo = []
            for i in range(len(nums)):
                memo.append([-1]*(target + 1))
            
            def dfs(i, t):
                if t == 0:
                    return True
                if i == len(nums) or target < 0:
                    return False
                if memo[i][t] != -1:
                    return memo[i][t]
                if dfs(i + 1, t):
                    memo[i][t] = True
                    return True
                if dfs(i + 1, t - nums[i]):
                    memo[i][t] = True
                    return True
                memo[i][t] = False
                return False
            return dfs(0, target)

        def solutionDPBottomUp():
            memo = []
            for i in range(len(nums) + 1):
                memo.append([False]*(target + 1))
                memo[i][0] = True
            
            for i in range(1, len(nums) + 1):
                for j in range(1, target + 1):
                    if nums[i - 1] <= j:
                        memo[i][j] = memo[i-1][j] or memo[i-1][j-nums[i-1]]
                    else:
                        memo[i][j] = memo[i-1][j]
            return memo[len(nums)][target]

        def solutionDPBottomUpSpaceOptmized():
            prev = [True] + [False]*target
            curr = [True] + [False]*target
            
            for i in range(1, len(nums) + 1):
                for j in range(1, target + 1):
                    if nums[i - 1] <= j:
                        curr[j] = prev[j] or prev[j-nums[i-1]]
                    else:
                        curr[j] = prev[j]
                prev = curr
                curr = [True] + [False]*target
            return prev[target]

        def solutionDPHashSet():
            achievable = {0}
            
            for n in nums:
                for t in achievable.copy():
                    curr = t + n
                    if curr in achievable:
                        continue
                    if curr == target:
                        return True
                    if curr < target:
                        achievable.add(curr)
            return False

        # return solutionRecursionOptmized()
        # return solutionDPTopDown()
        # return solutionDPBottomUp()
        # return solutionDPBottomUpSpaceOptmized()
        return solutionDPHashSet()