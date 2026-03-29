class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Since it must be in O(n) sorting is not an option
        if len(nums) <= 1:
            return len(nums)

        nums = set(nums)
        maxSequence = 1
        while nums:
            curr = 1
            popped = nums.pop()
            num = popped - 1
            while num in nums:
                nums.discard(num)
                num -= 1
                curr += 1
            num = popped + 1
            while num in nums:
                nums.discard(num)
                num += 1
                curr += 1
            maxSequence = max(maxSequence, curr)

        return maxSequence
