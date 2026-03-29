class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        targetBit = 1 << target
        targetMask = (1 << (target + 1)) - 1
        print(bin(targetMask), bin(targetBit))
        # targetMask =
        dp = 1 << 0
        print(bin(dp))

        for num in nums:
            if num > target:
                continue
            print(num, bin(dp), bin(dp << num), bin(dp | (dp << num)))
            dp |= dp << num
            dp &= targetMask
            if dp & targetBit:
                return True

        print(bin(dp), bin(targetBit), bin(dp & targetBit))
        return False
        # return (dp & (1 << target)) != 0