class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        asDict = {}
        for i in range(len(nums)):
            num = nums[i]
            if target - num in asDict:
                return [asDict[target-num], i]
            asDict[num] = i

        
