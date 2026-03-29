class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #Solution with O(n) space:
        numsSet = set(range(len(nums) + 1))
        for i in nums:
            numsSet.discard(i)
        return numsSet.pop()

        #Solution 2
        # Append None to nums
        # Then go replacing the number with the number in the correct position
        nums.append(None)
        for i in range(len(nums)):
            while nums[i] != i and nums[i] != None:
                tmp = nums[i]
                nums[i] = nums[tmp]
                nums[tmp] = tmp

        for i in range(len(nums)):
            if nums[i] == None:
                return i