class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # We may, at each time, do a dfs over the non-visited reachable points
        # Stop the index [n-1, n-1] is reached.
        upBitmask = 0b0001
        downBitmask = 0b0010
        leftBitmask = 0b0100
        rightBitmask = 0b1000
        exhaustedBitmask = 0b1111

        exhausting = [[0]*len(grid) for _ in range(len(grid))]
        visited = [[False]*len(grid) for _ in range(len(grid))]
        problemSpace = {grid[i][j] for i in range(len(grid)) for j in range(len(grid)) if grid[i][j] >= max(grid[0][0], grid[-1][-1])}

        problemSpace = sorted(problemSpace, reverse = True)
        for i in range(len(grid)):
            exhausting[0][i] ^= upBitmask
            exhausting[-1][i] ^= downBitmask
            exhausting[i][0] ^= leftBitmask
            exhausting[i][-1] ^= rightBitmask


        active = {(0,0)}
        t = problemSpace[-1]

        while (len(grid) - 1, len(grid) - 1) not in active:
            t = problemSpace.pop()
            newNodes = active.copy()
            while newNodes:
                x, y = newNodes.pop()
                moves = exhausting[x][y] ^ exhaustedBitmask
                # UP
                if moves & upBitmask and grid[x-1][y] <= t and not visited[x-1][y]:
                    moves ^= upBitmask
                    visited[x-1][y] = True
                    active.add((x-1, y))
                    newNodes.add((x-1, y))

                # DOWN
                if moves & downBitmask and grid[x+1][y] <= t and not visited[x+1][y]:
                    moves ^= downBitmask
                    visited[x+1][y] = True
                    active.add((x+1, y))
                    newNodes.add((x+1, y))

                # LEFT
                if moves & leftBitmask and grid[x][y-1] <= t and not visited[x][y-1]:
                    moves ^= leftBitmask
                    visited[x][y-1] = True
                    active.add((x, y-1))
                    newNodes.add((x, y-1))

                # RIGHT
                if moves & rightBitmask and grid[x][y+1] <= t and not visited[x][y+1]:
                    moves ^= rightBitmask
                    visited[x][y+1] = True
                    active.add((x, y+1))
                    newNodes.add((x, y+1))

                if moves == 0:
                    active.discard((x, y))
                    newNodes.discard((x, y))
        return t