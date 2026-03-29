import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # First let's find the point where it changes
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        if nums[0] < nums[-1]:
            # it is sorted
            index = bisect.bisect_left(nums, target)
            if index < len(nums) and nums[index] == target:
                return index

            return -1

        # Let's find the rotation point, i.e., where nums[i] < nums[i-1]
        left = 0
        right = len(nums)
        mid = (right - left) // 2

        while nums[mid] > nums[mid - 1]:
            if nums[mid] > nums[0]:
                # It is in the left side
                left = mid
            else:
                right = mid
            mid = (right - left) // 2 + left

        # now we know where it changes.
        val = 0
        if target >= nums[0]:
            # it is in the left
            val = bisect.bisect_left(nums, target, hi=mid)
            if val == mid:
                val = len(nums)
        else:
            # it is in the right
            val = bisect.bisect_left(nums, target, lo=mid)
        if val < len(nums) and nums[val] == target:
            return val
        return -1

