class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        dp = 1 << 0
        # print(bin(dp))

        for num in nums:
            # print(num, bin(dp), bin(dp << num), bin(dp | (dp << num)))
            dp |= dp << num

        # print(bin(dp), bin(1 << target), bin(dp & (1 << target)))
        return (dp & (1 << target)) != 0