class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # Let's start with a simple DFS solution
        # Then add a memory for repeated cases, using a hashmap because it may be sparse
        memory = {}
        def dfs(i, j):
            if (i, j) in memory:
                return memory[(i, j)]
            if i == len(s) and j < len(t):
                memory[(i, j)] = 0
            elif j == len(t):
                memory[(i, j)] = 1
            # Find the next possible
            elif s[i] != t[j]:
                memory[(i, j)] = dfs(i+1, j)
            else:
                # We know that s[i] == t[j], and we can either pick that or not
                memory[(i, j)] = dfs(i+1, j) + dfs(i+1, j+1)
            return memory[(i, j)]
        return dfs(0, 0)