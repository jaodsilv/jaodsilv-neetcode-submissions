class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        # This does not work because we may have numbers that shows 0 times
        # We can count the how many times a bit is there, the bits that show up more than the expected number are in the repeated number
        bits = [0]*14 # Assuming it fits in a 14bit int, given the restrictions that n <= 10000

        for num in nums:
            for i in range(14):
                bits[i] += num % 2
                num >>= 1
                if num == 0:
                    break
        res = []
        expected = 
        for i, count
        '''
        '''
        Slow and fast pointers
        '''
        # Let's treat this array as a Linked List and we need to find the loop
        # Then we can use the fast and slow pointers technique
        # Instead of pointers we have indexes
        slow = fast = 0
        slow = nums[slow]
        fast = nums[nums[fast]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        # With that we find that there is a loop
        # Now we need to find the head of the loop
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow