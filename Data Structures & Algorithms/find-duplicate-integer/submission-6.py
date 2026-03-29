class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Bit Manipulation
        n = len(nums)
        res = 0
        for b in range(14):
            x = 0
            mask = 1 << b
            for num in nums:
                if num & mask:
                    x += 1
            for num in range(1, n):
                if num & mask:
                    x -= 1
            if x > 0:
                res |= mask
        return res
        '''
        # Brute Force
        for i in range(1, len(nums)):
            found = False
            for j in nums:
                if j == i:
                    if found:
                        return j
                    else:
                        found = True
        '''