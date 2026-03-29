import bisect

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Number can be negative, therefore they might be greater than target, therefore we can't filter it.
        # Let's start with 2 pointers from the corners
        # We know the solution always exist and only one
        left, right = 0, len(numbers) - 1
        base = numbers[left] + numbers[right]
        if base == target:
            return [left + 1, right + 1]
        attempts = 0
        while numbers[left] + numbers[right] != target and attempts < 10:
            attempts += 1
            print(left, right)
            if target < numbers[left] + numbers[right]:
                right = bisect.bisect_right(numbers, target - numbers[left], lo=left + 1, hi=right) - 1
            elif target > numbers[left] + numbers[right]:
                left = bisect.bisect_left(numbers, target - numbers[right], lo=left + 1, hi=right)
        return [left + 1, right + 1]
