from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # This resumes to calculating the maximum minimum distance from every fresh fruit to any rotten fruit
        # We can start by the rotten and use a BFS. Once all fruits are rotten we return the "time"
        queue = deque()
        freshCount = 0
        for i, r in enumerate(grid):
            for j, v in enumerate(r):
                if v == 2:
                    queue.append((i, j))
                elif v == 1:
                    freshCount += 1
        time = 0
        while freshCount and queue:
            time += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                if i > 0 and grid[i-1][j] == 1:
                    grid[i-1][j] = 2
                    queue.append((i-1, j))
                    freshCount -= 1
                if j > 0 and grid[i][j-1] == 1:
                    grid[i][j-1] = 2
                    queue.append((i, j-1))
                    freshCount -= 1
                if i < len(grid) - 1 and grid[i+1][j] == 1:
                    grid[i+1][j] = 2
                    queue.append((i+1, j))
                    freshCount -= 1
                if j < len(grid[0]) - 1 and grid[i][j+1] == 1:
                    grid[i][j+1] = 2
                    queue.append((i, j+1))
                    freshCount -= 1
                
        return time if freshCount == 0 else -1
