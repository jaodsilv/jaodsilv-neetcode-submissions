import bisect

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Number can be negative, therefore they might be greater than target, therefore we can't filter it.
        # Let's start with 2 pointers from the corners
        # We know the solution always exist and only one
        left, right = 0, len(numbers) - 1
        # attempts = 0
        while numbers[left] + numbers[right] != target:# and attempts < 10:
            # attempts += 1
            # print(left, right)
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
        return [left + 1, right + 1]
