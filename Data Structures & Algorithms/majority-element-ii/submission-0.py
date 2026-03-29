from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        target = n//3
        counter = defaultdict(int)
        res = []
        for num in nums[:((2*n) // 3)+1]:
            counter[num] += 1
        for num, count in counter.items():
            if count > target:
                res.append(num)
        for num in res:
            del counter[num]
        # Any number not in counter cannot reach n//3 after that
        for num in nums[((2*n) // 3)+1:]:
            if num in counter:
                counter[num] += 1
        for num, count in counter.items():
            if count > target:
                res.append(num)
        return res