from collections import Counter, defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return [nums[0]]

        counter = Counter(nums) # O(n)
        maxFreq = max(counter.values())
        freqs = defaultdict(list)
        for i, f in counter.items():
            freqs[f].append(i)
        res = []
        for i in range(maxFreq, 0, -1):
            if len(res) == k:
                return res
            if i in freqs:
                res.extend(freqs[i])
        return res
