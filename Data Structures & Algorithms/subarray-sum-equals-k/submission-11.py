from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)
        counter[0] = 1
        prefixSum = 0
        total = 0
        for n in nums:
            prefixSum += n
            # prefixSum - prev = k
            total += counter[prefixSum-k]
            counter[prefixSum] += 1
        return total