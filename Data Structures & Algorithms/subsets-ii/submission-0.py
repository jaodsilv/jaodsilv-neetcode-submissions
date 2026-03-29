class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # Given they are sorted, we can "skip" repeated choices easily

        res = [[]]

        i = 0
        while i < len(nums):
            # Let's see how many element of the same value nums[i] exist:
            j = i + 1
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            count = j - i

            for k in range(len(res)):
                subset = res[k].copy()
                subset.append(nums[i])
                res.append(subset)
                for _ in range(count - 1):
                    subset = subset.copy()
                    subset.append(nums[i])
                    res.append(subset)
            i = j

        return res
