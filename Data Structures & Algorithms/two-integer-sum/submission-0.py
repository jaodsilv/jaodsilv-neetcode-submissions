class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sort = sorted(nums)
        i = 0
        j = 1
        vall, valh = None, None
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if sort[i] + sort[j] == target:
                    vall = sort[i]
                    valh = sort[j]
                    break
                if sort[i] + sort[j] > target:
                    break
            if vall is not None:
                break
        for i in range(len(nums)):
            if nums[i] == vall:
                vall = i
                break
        for i in range(len(nums)):
            if nums[i] == valh:
                valr = i
        return [min(vall, valr), max(vall, valr)]
