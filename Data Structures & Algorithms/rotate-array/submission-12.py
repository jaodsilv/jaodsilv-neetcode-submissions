import math

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Let's do it in O(1) space and O(n) time
        n = len(nums)
        k %= n
        gcd = math.gcd(k, len(nums))
        for i in range(gcd):
            last = nums[i]
            j = i + k
            while j != i:
                nums[j], last = last, nums[j]
                j = (j + k) % n
            nums[i] = last
