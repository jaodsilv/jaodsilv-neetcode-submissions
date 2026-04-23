class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        # Move everybody k to the right and move the last k to the beginning.
        nums[:] = nums[n-k:] + nums[:n-k]
