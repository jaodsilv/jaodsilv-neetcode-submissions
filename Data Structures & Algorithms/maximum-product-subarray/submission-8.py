class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Rule 1: When there are zeroes, then either the maximum will be 0 or the maximum must not include zeroes
        # Rule 2: To be zero it must contain only zeroes and negatives, and the negatives, if any, must be isolated by zeroes.
        # Rule 3: Negative numbers must be included in pairs, so they become positive
        if len(nums) == 1:
            return nums[0]
        
        # Blocks isolated by zeroes
        currProd = 1
        maxProdTilLastNeg = 0
        maxProdAfterFirstNeg = 0
        count = 0
        maxProd = nums[0]
        # O(n) time
        for n in nums:
            if n == 0:
                maxProd = max(maxProd, 0)
                if count > 1:
                    maxProd = max(maxProd, currProd, maxProdAfterFirstNeg, maxProdTilLastNeg)
                elif count == 1:
                    maxProd = max(maxProd, currProd)
                currProd = 1
                maxProdTilLastNeg = 0
                maxProdAfterFirstNeg = 0
                count = 0
            else:
                count += 1
                if maxProdAfterFirstNeg:
                    maxProdAfterFirstNeg *= n
                if n < 0:
                    maxProdTilLastNeg = currProd
                    if not maxProdAfterFirstNeg:
                        maxProdAfterFirstNeg = 1
                if count == 1:
                    currProd = n
                else:
                    currProd *= n
        if count > 1:
            maxProd = max(maxProd, currProd, maxProdAfterFirstNeg, maxProdTilLastNeg)
        elif count == 1:
            maxProd = max(maxProd, currProd)
        return maxProd
