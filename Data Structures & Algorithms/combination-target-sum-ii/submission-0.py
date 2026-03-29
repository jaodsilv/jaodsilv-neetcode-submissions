import bisect

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #O(n*log(n))
        candidates.sort()

        res = [[]]
        sums = [0]
        prev = None
        L = 0
        # With them in ascending order we know when to stop for each group
        for i in range(len(candidates)):
            L2 = len(res)
            d = candidates[i]
            for j in range(L if d == prev else 0, len(res)):
                if d + sums[j] <= target:
                    sums.append(d + sums[j])
                    s = res[j].copy()
                    s.append(d)
                    res.append(s)
            L = L2
            prev = d

        res2 = []
        for i in range(len(sums)):
            if sums[i] == target:
                res2.append(res[i])

        return res2
