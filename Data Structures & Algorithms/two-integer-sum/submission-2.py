from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = defaultdict(list)
        for i in range(len(nums)):
            myMap[nums[i]].append(i)
        
        # Lets test first for 2 equal numbers:
        if target % 2 == 0 and target // 2 in myMap:
            if len(myMap[target // 2]) >= 2:
                return myMap[target // 2][0:2]
            else:
                del myMap[target // 2]

        print(myMap)
        for i in nums:
            if target-i != i and target - i in myMap:
                print(i, target-i)
                return [min(myMap[i][0], myMap[target-i][0]), max(myMap[i][0], myMap[target-i][0])]
