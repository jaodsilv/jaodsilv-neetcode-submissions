class Solution:
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

        res = []

        def combineRecursive(cur, total, i):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target: # or len(cur) > 15:
                return

            cur.append(nums[i])
            combineRecursive(cur, total + nums[i], i)
            cur.pop()
            combineRecursive(cur, total, i + 1)

        combineRecursive([], 0, 0)
        return res
