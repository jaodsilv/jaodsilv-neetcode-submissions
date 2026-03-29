class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        longest = 1

        '''
        O(n*log(n)) time solution:
        '''
        '''
        nums.sort()

        last = nums[0]
        curr = 1
        for i in nums[1:]:
            if i == last + 1:
                curr += 1
            else:
                if curr > longest:
                    longest = curr
                curr = 1
            last = i
        if curr > longest:
            longest = curr
        return longest
        '''
        '''
        O(n) time solution:
        '''
        # We can either start from the first element or from a local minimum
        # An O(n*log(n)) is easy, just sort then find the biggest sequence.
        # Without sorting we must rely in some other information
        # 
        # What if we get contiguous elements as soon as they appear, then merge them in a second run
        # nums has at most 1000 elements
        # Therefore, any two elements should be at most distance to be in the same sequence.
        # Let's create groups for every 1000 we are looking into. However, the numbers can range from -10e9 to 10e9, which means that there is enough room for a 1000 groups
        # We may build as we find, but, then, we need to merge groups afterwards

        numsSet = set(nums)
        starts = set()
        for i in nums:
            if i - 1 not in numsSet:
                starts.add(i) # Worst case starts have the same elements as nums
        longest = 1
        for i in starts:
            cur = 1
            j = i
            while j + 1 in numsSet:
                cur += 1
                j += 1
            if cur > longest:
                longest = cur
        return longest
