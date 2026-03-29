class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]

        if len(nums) == 2:
            return nums[-1]

        # Positions:
        # [a,...,b,c,...,d]
        # I need to find c using a binary search

        leftmost = 0
        rightmost = len(nums)

        while leftmost < rightmost - 1:
            position = (rightmost - leftmost) // 2 + leftmost
            if nums[position] < nums[0]:
                rightmost = position
            elif nums[position] > nums[0]:
                leftmost = position

        return nums[rightmost]