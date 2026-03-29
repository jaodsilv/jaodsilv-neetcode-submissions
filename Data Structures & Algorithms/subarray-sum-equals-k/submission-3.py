from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        prefixSum = defaultdict(int)
        prefixSum[0] = 1 # position 0 has sum 0
        for n in nums:
            curSum += n
            diff = curSum - k
            res += prefixSum[diff]
            prefixSum[curSum] += 1
        return res