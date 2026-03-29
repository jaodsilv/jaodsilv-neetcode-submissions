class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0
        if len(t) == len(s):
            return 1 if t == s else 0
        
        # Brute Force
        count = 0
        letters = {}
        for i, c in enumerate(s):
            if c not in letters:
                letters[c] = [0, []]
            letters[c][1].append(i)

        def dfs(i, j):
            if i == len(t):
                return 1

            c = t[i]
            posis = letters[c]
            count = 0
            initial = posis[0]
            for k in range(initial, len(posis[1])):
                pos = posis[1][k]
                if pos >= j:
                    count += dfs(i+1, pos+1)
                posis[0] += 1
            posis[0] = initial
            return count
        return dfs(0, 0)