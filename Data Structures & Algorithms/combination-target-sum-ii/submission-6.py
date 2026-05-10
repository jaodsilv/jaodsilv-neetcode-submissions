class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        values = [0]*(target + 1)
        for c in candidates:
            if c <= target:
                values[c] += 1

        # They are all positives, therefore we can discard any value above target
        res = [(0, [])]
        finalRes = set()
        for i, c in enumerate(values):
            if c == 0:
                continue
            for k in range(len(res)):
                s, r = res[k]
                p = []
                for j in range(1, c+1):
                    if j*i > target:
                        break
                    p.append(i)
                    if s + j*i == target:
                        finalRes.add(tuple(r + p))
                    elif s + j*i < target:
                        res.append((s + j*i, r + p))
            
        return [list(r) for r in finalRes]
