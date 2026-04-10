from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = [0]
        counter = defaultdict(int)
        count = 0
        for n in nums:
            counter[prefixSum[-1]] += 1
            prefixSum.append(prefixSum[-1] + n)
            # prefix[j] - prefix[i] = k => prefix[i] = prefix[j] - k
            count += counter[prefixSum[-1] - k]
        return count
