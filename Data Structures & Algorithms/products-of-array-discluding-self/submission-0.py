class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        twoZeros = False
        firstZero = None if nums[0] != 0 else 0
        for i in range(1, len(nums)):
            num = nums[i]
            if num == 0:
                if firstZero is None:
                    firstZero = i
                    prod *= nums[0]
                else:
                    prod = 0
                    twoZeros = True
                    break
            else:
                prod *= num


        if twoZeros == True:
            return [0]*len(nums)

        if firstZero is None:
            output = nums.copy()
            output[0] = prod
            for i in range(1, len(output)):
                output[i] = (prod // nums[i]) * nums[0]
        else:
            output = [0] * len(nums)
            output[firstZero] = prod

        return output
