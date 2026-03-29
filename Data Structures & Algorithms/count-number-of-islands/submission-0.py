class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        def deleteLand(i, j):
            grid[i][j] = 0
            if i > 0 and grid[i - 1][j] == '1':
                deleteLand(i - 1, j)
            if j > 0 and grid[i][j - 1] == '1':
                deleteLand(i, j - 1)
            if i < len(grid) - 1 and grid[i + 1][j] == '1':
                deleteLand(i + 1, j)
            if j < len(grid[0]) - 1 and grid[i][j + 1] == '1':
                return deleteLand(i, j + 1)
            return j

        for i in range(len(grid)):
            j = 0
            while j < len(grid[0]):
                if grid[i][j] == '1':
                    count += 1
                    j = deleteLand(i, j)
                j += 1
        
        return count