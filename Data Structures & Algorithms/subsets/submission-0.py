class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            for r in range(len(res)):
                prev = res[r].copy()
                prev.append(num)
                res.append(prev)
        return res