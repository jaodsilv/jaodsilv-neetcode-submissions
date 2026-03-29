class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def findPath(prev, i, j, dp):
            if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] <= prev:
                return 0
            if dp[i][j] > 0:
                return dp[i][j]
            v = matrix[i][j]
            dp[i][j] = 1 + max(findPath(v, i - 1, j, dp), findPath(v, i + 1, j, dp), findPath(v, i, j - 1, dp), findPath(v, i, j + 1, dp))
            return dp[i][j]
        dp = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        maxPath = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                maxPath = max(maxPath, findPath(-1, i, j, dp))
        return maxPath