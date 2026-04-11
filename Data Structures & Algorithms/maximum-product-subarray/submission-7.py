class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Rule 1: When there are zeroes, then either the maximum will be 0 or the maximum must not include zeroes
        # Rule 2: To be zero it must contain only zeroes and negatives, and the negatives, if any, must be isolated by zeroes.
        # Rule 3: Negative numbers must be included in pairs, so they become positive
        if len(nums) == 1:
            return nums[0]
        
        # Blocks isolated by zeroes
        blocks = [[]]
        negs = [[0, None, None]]
        for n in nums:
            if n == 0:
                if len(blocks[-1]) > 0:
                    blocks.append([])
                    negs.append([0, None, None])
            else:
                if n < 0:
                    negs[-1][0] += 1
                    if negs[-1][1] is None:
                        negs[-1][1] = len(blocks[-1])
                    negs[-1][2] = len(blocks[-1])
                blocks[-1].append(n)

        hasZero = False if len(blocks) == 1 and blocks[0] else True

        if len(blocks[-1]) == 0:
            blocks.pop()
        if not blocks:
            return 0
        maxProd = 0
        # print(len(blocks))
        # print(negs)
        for block, negTriple in zip(blocks, negs):
            neg, firstNeg, lastNeg = negTriple
            if neg % 2 == 0:
                # print(block)
                curr = 1
                for n in block:
                    curr *= n
                maxProd = max(maxProd, curr)
            elif len(block) > 1:
                currL = 1
                currR = 1
                hasPos = False
                for i, n in enumerate(block):
                    if n > 0:
                        hasPos = True
                    if i < lastNeg:
                        currR *= n
                    if i > firstNeg:
                        currL *= n
                maxProd = max(maxProd, currR, currL)

        return maxProd
