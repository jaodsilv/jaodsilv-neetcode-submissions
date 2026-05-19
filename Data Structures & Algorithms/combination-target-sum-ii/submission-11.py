class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        cCand = [0]*51
        for candidate in candidates:
            cCand[candidate] += 1

        res = []
        def dfs(curr, total, i):
            if total > target:
                return
            if total == target:
                print('found it')
                res.append(curr.copy())
                return
            if i >= len(cCand):
                return
            # Let's start not taking any from this:
            dfs(curr, total, i+1)
            for _ in range(cCand[i]):
                curr.append(i)
                total += i
                if total > target:
                    break
                dfs(curr, total, i+1)
            while curr and curr[-1] == i:
                curr.pop()
        dfs([], 0, 1)
        return res