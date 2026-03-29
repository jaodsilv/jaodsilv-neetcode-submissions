class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        target = 1 << target
        # targetMask =
        dp = 1 << 0
        print(bin(dp))

        for num in nums:
            print(num, bin(dp), bin(dp << num), bin(dp | (dp << num)))
            dp |= dp << num
            if dp & target:
                return True

        print(bin(dp), bin(target), bin(dp & target))
        return False
        # return (dp & (1 << target)) != 0