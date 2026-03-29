from collections import defaultdict
from bisect import bisect_left

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Solution 1
        # We can have all of them 0, or at least one number must be positive and one must be negative
        #asDict = defaultdict(list)
        #for i in range(len(nums)):
        #    asDict[nums[i]].append(i)

        #res = set()

        # Now it is missing only triples in which all numbers are different
        #for i in range(len(nums) - 2):
        #    for j in range(i + 1, len(nums) - 1):
        #        other = -(nums[i] + nums[j])
        #        if other in asDict:
        #            for index in asDict[other]:
        #                if index > j:
        #                    res.add(tuple(sorted([nums[i], nums[j], other])))
        #                    break

        nums.sort()
        print(nums)
        if nums[0] > 0 or nums[-1] < 0:
            return []

        res = set()

        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break

            # let's find all pairs of numbers which the sum is -i
            # Since it is sorted, we can find the middle point in O(log(n))
            # Then we can go left or right with 2 pointers until either left get to i or right gets to the end. Which is O(n).
            mid = math.ceil(-nums[i] / 2)
            j = bisect_left(nums, mid, lo = i+1)
            if nums[j] > -nums[i] / 2:
                j -= 1
            k = j + 1
            while k < len(nums) and j > i:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    res.add((nums[i], nums[j], nums[k]))
                    j -= 1
                    k += 1
                elif total > 0:
                    j -= 1
                else:
                    k += 1


        return [list(x) for x in res]

