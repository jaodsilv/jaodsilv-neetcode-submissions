class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        # Treat as a LinkedList
        # Fast and Slow Pointers
        # Is there a way where the repeated number is in a disconnected part?
        # No, because we start at a position not in the valid values, it makes every move shifted, either we have a loop or a non-valid number
        slow = fast = 0

        # Find loop exists in LinkedList
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Find head of the loop
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
        '''

        # Bit Manipulation
        # O(1) space, O(math.ceil(log(max(n), 2)) * n) = O(14*n) = O(n) time complexity
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