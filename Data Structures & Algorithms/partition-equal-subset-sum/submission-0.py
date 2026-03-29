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
