class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # To get it in O(1) space and O(n) time we need a voting algorithm
        major = None
        count = 0
        for n in nums:
            if n == major:
                count += 1
            elif count == 0:
                count = 1
                major = n
            else:
                count -= 1
        return major

