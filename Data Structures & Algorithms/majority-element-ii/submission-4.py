class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) <= 2:
            return nums
        # MORE THAN (n // 3) only 2 elements are possible.
        # Let's use a voting algorithm
        n1 = None
        v1 = 0
        n2 = None
        v2 = 0
        for n in nums:
            print(n1, v1, n2, v2)
            if n == n1:
                v1 += 1
            elif n == n2:
                v2 += 1
            else:
                if v1 <= 0:
                    v1 = 1
                    n1 = n
                elif v2 <= 0:
                    v2 = 1
                    n2 = n
                else:
                    v1 -= 1
                    v2 -= 1
        print(n1, n2)
        v1 = 0
        v2 = 0
        for n in nums:
            if n == n1:
                v1 += 1
            if n == n2:
                v2 += 1
        res = []
        if v1 > len(nums) // 3:
            res.append(n1)
        if v2 > len(nums) // 3:
            res.append(n2)
        return res

