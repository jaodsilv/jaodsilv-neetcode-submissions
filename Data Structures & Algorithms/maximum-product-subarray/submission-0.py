class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Different from sums, we can easily revert a negative with another negative.
        # We can never revert a 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            if nums[0] * nums[1] > 0:
                return nums[0] * nums[1]
            else:
                return max(nums)


        candidate = max(nums)
        if candidate == 0:
            hasNonZero = False
            for i in range(len(nums)):
                val = nums[i]
                if val != 0 and (val > 0 or (i < len(nums) - 1 and nums[i+1] != 0)):
                        hasNonZero = True
                        break

            if not hasNonZero:
                return 0

        i = 0
        while i < len(nums):
            while i < len(nums) and nums[i] == 0:
                i += 1
            
            if i == len(nums):
                return candidate

            init = i
            negatives = []
            prods = [nums[i]]
            if nums[i] < 0:
                negatives.append(i)

            i += 1
            while i < len(nums) and nums[i] != 0:
                prods.append(nums[i] * prods[-1])
                if nums[i] < 0:
                    if len(negatives) <= 1:
                        negatives.append(i - init)
                    else:
                        negatives[1] = i - init
                i += 1

            if prods[-1] > 0:
                candidate = max(candidate, prods[-1])
            elif len(prods) == 1:
                continue
            elif len(negatives) == 1:
                if negatives[0] == 0:
                    candidate = max(candidate, prods[-1] // prods[0])
                elif negatives[0] == len(prods) - 1:
                    candidate = max(candidate, prods[-2])
                else:
                    candidate = max(candidate, prods[negatives[0] - 1], prods[-1] // prods[negatives[0]])
            else:
                candidate = max(candidate, prods[negatives[1] - 1], prods[-1] // prods[negatives[0]])
            
        return candidate
