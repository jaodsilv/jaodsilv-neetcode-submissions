class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        # nums = set(nums)
        def generate(R, curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            L = []
            while R:
                num = R.pop()
                curr.append(num)
                generate(L + R, curr)
                curr.pop()
                L.append(num)
        generate(nums.copy(), [])
        return res