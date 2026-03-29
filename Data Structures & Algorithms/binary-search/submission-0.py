class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while right - left > 1:
            mid = (left + right) // 2
            if mid >= len(nums):
                return -1
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return left if left < len(nums) and nums[left] == target else -1