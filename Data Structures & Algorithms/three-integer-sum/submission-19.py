import bisect

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # O(nlogn)
        if nums[0] > 0 or nums[-1] < 0:
            return []

        if nums[0] == 0 and nums[2] > 0:
            return []

        if nums[-1] == 0 and nums[-3] > 0:
            return []

        firstNonNegative = bisect.bisect_left(nums, 0)

        res = []
        if firstNonNegative < len(nums) - 2 and nums[firstNonNegative + 2] == 0:
            res.append([0,0,0])

        prev = nums[0] - 1
        for i in range(firstNonNegative):
            if nums[i] == prev:
                continue
            prev = nums[i]

            # Search all pairs that sum nums[i] whose indexes are greater than i
            target = -nums[i]
            L = i + 1
            R = len(nums) - 1
            while L < R:
                valL = nums[L]
                valR = nums[R]
                if valL + valR < target:
                    while L < R and nums[L] == valL:
                        L += 1
                elif valL + valR > target:
                    while nums[R] == valR:
                        R -= 1
                else:
                    res.append([-target, valL, valR])
                    while L < R and nums[L] == valL:
                        L += 1
                    while nums[R] == valR:
                        R -= 1
        return res