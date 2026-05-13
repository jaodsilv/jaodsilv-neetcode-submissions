class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        '''

                      1, 2, -3   4  -5
        afterFirstNeg N, N, N,   4 -20
        curr          1, 2, -6 -24 120
        maxProd       N  N  2    2   4  120

        We have to keep the products:
          1. from after the last 0 or beginning
          2. from after the first negative after a 0 or beginning
        '''
        maxProd = max(nums)
        curr = 0
        afterFirstNeg = 0
        for num in nums:
            if num == 0:
                if curr:
                    maxProd = max(maxProd, curr)
                    curr = 0
                if afterFirstNeg:
                    maxProd = max(maxProd, afterFirstNeg)
                    afterFirstNeg = 0
            else:
                if afterFirstNeg:
                    afterFirstNeg *= num
                    maxProd = max(maxProd, curr)
                elif curr < 0:
                    afterFirstNeg = num
                if curr:
                    if num < 0:
                        maxProd = max(maxProd, curr)
                    curr *= num
                    maxProd = max(maxProd, curr)
                else:
                    curr = num
                    # max prod is alredy bigger than or equals to any isolated number
                    # maxProd = max(maxProd, curr)
            print(maxProd, curr, afterFirstNeg)
        if curr:
            maxProd = max(maxProd, curr)
        if afterFirstNeg:
            maxProd = max(maxProd, afterFirstNeg)
        return maxProd

                
