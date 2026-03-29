class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # Let's build 3 arrays
        # One containing the maximum product that includes the current index
        # One containing the maximum absolute product that includes the current index, which, except for zeroes, they never decrease
        # When the result will be 0: When at most one value is below 0, and the other values are 0
        hasNegative = False
        maxIsZero = False
        for val in nums:
            if val < 0:
                if hasNegative:
                    maxIsZero = False
                    break
                else:
                    hasNegative = True
            elif val > 0:
                maxIsZero = False
                break
            else:
                maxIsZero = True

        if maxIsZero:
            return 0


        maxPosProd = [nums[0]]
        maxNegProd = [nums[0]]

        for val in nums[1:]:
            latestMaxNegProd = maxNegProd[-1]
            latestMaxPosProd = maxPosProd[-1]
            maxPosProd.append(max(latestMaxPosProd*val, val, latestMaxNegProd*val))
            maxNegProd.append(min(latestMaxPosProd*val, val, latestMaxNegProd*val))
        print(maxPosProd)
        print(maxNegProd)

        return max(maxPosProd)