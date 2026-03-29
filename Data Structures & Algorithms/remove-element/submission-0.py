class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        shift = 0
        for i in range(len(nums)):
            if nums[i] == val:
                shift += 1
            elif shift:
                nums[i-shift] = nums[i]
        for _ in range(shift):
            nums.pop()
        return len(nums)