class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        print(nums)
        for i in range(n):
            if nums[i] < 0 or nums[i] > n:
                nums[i] = 0
        print(nums)

        for i in range(n):
            val = abs(nums[i])
            if 0 < val <= n: # val > 0 Means the value is within the desired range
                if nums[val - 1] > 0:
                    # marking a negative number here indicates the presence of val in the array
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    # A 0 value here the original value was out of the desired range, so, how to mark val is present?
                    # Add a dummy value that IS out of range or we could set the value to -val as well since we know val is present
                    nums[val - 1] = -val
                # If it is negative it means it have been found previously

        print(nums)
        for i in range(1, n + 1):
            if nums[i - 1] >= 0: # i.e., find the first element that have not been modified
                return i

        return n + 1