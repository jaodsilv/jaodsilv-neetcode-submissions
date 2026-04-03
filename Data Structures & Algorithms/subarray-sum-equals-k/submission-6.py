from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = [0]
        for n in nums:
            prefixSum.append(prefixSum[-1] + n)
        prefixMap = defaultdict(int)
        count = 0
        for i in range(len(prefixSum)):
            target = prefixSum[i] - k
            count += prefixMap[target]
            prefixMap[prefixSum[i]] += 1
        return count