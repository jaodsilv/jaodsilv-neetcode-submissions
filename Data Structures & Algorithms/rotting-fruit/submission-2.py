from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # This is a problem of finding the distant of the point that is farthest to any rotten fruit
        # 0 means it is not a path
        # 2 means it is a start point
        # 1 means it is a end point (or vice-versa, it doesn't matter)

        # Let's do a BFS to calculate those distances simultaneously

        rotten = []
        freshCount = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    grid[i][j] = -1
                elif grid[i][j] == 1:
                    freshCount += 1
                    grid[i][j] = 101
                elif grid[i][j] == 2:
                    grid[i][j] = 0
                    rotten.append((i, j))

        if freshCount == 0:
            return 0

        queue = deque(rotten)
        
        # Let's use the actual dist with a 2 increased value to difer from fresh and empty
        dist = 1
        while queue:
            print(grid)
            for _ in range(len(queue)):
                i, j = queue.popleft()
                if i > 0 and grid[i-1][j] > dist:
                    grid[i-1][j] = dist
                    queue.append((i-1, j))
                    freshCount -= 1
                if j > 0 and grid[i][j-1] > dist:
                    grid[i][j-1] = dist
                    queue.append((i, j-1))
                    freshCount -= 1
                if i < len(grid) - 1 and grid[i + 1][j] > dist:
                    grid[i+1][j] = dist
                    queue.append((i+1, j))
                    freshCount -= 1
                if j < len(grid[0]) - 1 and grid[i][j + 1] > dist:
                    grid[i][j + 1] = dist
                    queue.append((i, j + 1))
                    freshCount -= 1
            dist += 1
        print(grid)
        return dist - 2 if freshCount == 0 else -1


