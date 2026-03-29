class Solution:
    def combineRecursive(self, nums, target, res, curr):
        for i in nums:
            if i + curr > target:
                return
            if i + curr == target:
                yield res + [i]
            else:
                combs = self.combineRecursive(nums, target, res + [i], i + curr)
                for comb in combs:
                    yield comb

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) == 1:
            if target % nums[0] != 0:
                return []
            else:
                return [[nums[0]] * (target // nums[0])]
        # Let's eliminate the impossibles
        nums = [i for i in nums if i <= target]
        # Let's sort the numbers # O(logn)
        nums.sort()

        combs = self.combineRecursive(nums, target, [], 0)
        resSet = set()
        for comb in combs:
            resSet.add(tuple(sorted(comb)))
        return list([list(x) for x in resSet])
