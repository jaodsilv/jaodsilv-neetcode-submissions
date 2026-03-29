class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == val:
                n -= 1
                nums[i] = nums[n]
            else:
                i += 1
        return n
    def removeElementV1(self, nums: List[int], val: int) -> int:
        shift = 0
        for i in range(len(nums)):
            if nums[i] == val:
                shift += 1
            elif shift:
                nums[i-shift] = nums[i]
        for _ in range(shift):
            nums.pop()
        return len(nums)