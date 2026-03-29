class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        

        def dfs(curr, notVisited, res):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for i in notVisited.copy():
                notVisited.discard(i)
                curr.append(nums[i])
                dfs(curr, notVisited, res)
                curr.pop()
                notVisited.add(i)

        res = []
        dfs([], set(range(len(nums))), res)
        return res