from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) <= 2:
            return list(set(nums))
        '''
        # Boyer-Moore Voting Algorithm
        4,3,3,2, | 2,2,2,5,5,5        
        n1 = 4;c1 = 1
        n2 = 3;c2 = 1
        c2 = 2
        c1 = 0;c2=1
        ...
        c2 = 4
        c1=2;c2=3
        c1=1;c2=2
        c1=0;c2=1
        '''

        target = len(nums) // 3

        n1 = nums[0]
        n2 = None
        c1 = c2 = 0

        for i in nums:
            if i == n1:
                c1 += 1
            elif i == n2:
                c2 += 1
            elif c1 == 0:
                n1 = i
                c1 = 1
            elif c2 == 0:
                n2 = i
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1

        if n2 is None:
            return [n1]

        c1 = 0
        c2 = 0

        for n in nums:
            if n == n1:
                c1 += 1
            if n == n2:
                c2 += 1

        res = []
        if c1 > target:
            res.append(n1)
        if c2 > target:
            res.append(n2)
        return res
