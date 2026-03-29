from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #nums.sort()
        #if nums[0] > 0 or nums[-1] < 0:
        #    return []
        
        # We can have all of them 0, or at least one number must be positive and one must be negative
        asDict = defaultdict(list)
        for i in range(len(nums)):
            asDict[nums[i]].append(i)

        res = set()
        #if len(asDict[0]) >= 3:
        #    res.add((0,0,0))

        # First let's check with all number which appear more than once in the list
        #for kv in asDict.items():
        #    if len(kv[1]) >= 2 and -2*kv[0] in asDict:
        #        res.add((min(kv[0], -2*kv[0]), kv[0], max(kv[0], -2*kv[0])))

        # Now it is missing only triples in which all numbers are different
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                other = -(nums[i] + nums[j])
                if other in asDict:
                    for index in asDict[other]:
                        if index > j:
                            res.add(tuple(sorted([nums[i], nums[j], other])))
                            break
        
        return [list(x) for x in res]

        