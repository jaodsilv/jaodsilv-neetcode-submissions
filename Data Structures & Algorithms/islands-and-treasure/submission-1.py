from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647

        # We can do BFS starting from each tresure chest to find the distance
        chests = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    chests.append((i, j))
        
        queue = deque(chests)
        dist = 1
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                # We check strictly higher than dist and update the value before enqueue to avoid appending the item twice
                # UP
                if i > 0 and grid[i-1][j] > dist:
                    grid[i-1][j] = dist
                    queue.append((i-1, j))
                # LEFT
                if j > 0 and grid[i][j-1] > dist:
                    grid[i][j-1] = dist
                    queue.append((i, j-1))
                # DOWN
                if i < len(grid) - 1 and grid[i+1][j] > dist:
                    grid[i+1][j] = dist
                    queue.append((i+1, j))
                # RIGHT
                if j < len(grid[0]) - 1 and grid[i][j+1] > dist:
                    grid[i][j+1] = dist
                    queue.append((i, j+1))

            dist += 1
