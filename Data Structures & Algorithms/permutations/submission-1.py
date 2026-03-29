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

        def generate2(idx):
            if idx == len(nums):
                res.append(nums.copy())
            
            for i in range(idx, len(nums)):
                nums[idx], nums[i] = nums[i], nums[idx]
                generate2(idx + 1)
                nums[idx], nums[i] = nums[i], nums[idx]

        # generate(nums.copy(), [])
        generate2(0)
        return res