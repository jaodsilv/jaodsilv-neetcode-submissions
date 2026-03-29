class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        def solutionBinarySearch():
            def isValid(i, j):
                return i >= 0 and j >= 0 and i < len(grid) and j < len(grid)

            def dfs(t, i, j, visited):
                if not isValid(i, j) or grid[i][j] > t or (i, j) in visited:
                    return False
                if i == j == len(grid) - 1:
                    return True

                visited.add((i, j))
                return dfs(t, i - 1, j, visited) or dfs(t, i + 1, j, visited) or dfs(t, i, j - 1, visited) or dfs(t, i, j + 1, visited)

            L = max(grid[0][0], grid[-1][-1])
            R = max([max(row) for row in grid]) + 1
            t = (R + L) // 2
            while True:
                # t = (R + L) // 2
                print(L, R, t)
                if dfs(t, 0, 0, set()):
                    R = t # We must consider the current t as a valid value, but we don't need to test it again
                else:
                    L = t + 1 # t is not a possible value
                tmp = t
                t = (R + L) // 2
                if tmp == t:
                    return t
            return t
        return solutionBinarySearch()