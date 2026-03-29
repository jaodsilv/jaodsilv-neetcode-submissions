from collections import defaultdict
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # We may, at each time, do a dfs over the non-visited reachable points
        # Stop the index [n-1, n-1] is reached.
        if len(grid) == 1:
            return grid[0][0]

        upBitmask = 0b0001
        downBitmask = 0b0010
        leftBitmask = 0b0100
        rightBitmask = 0b1000
        exhaustedBitmask = 0b1111

        exhausting = [[0]*len(grid) for _ in range(len(grid))]
        for i in range(len(grid)):
            exhausting[0][i] ^= upBitmask
            exhausting[-1][i] ^= downBitmask
            exhausting[i][0] ^= leftBitmask
            exhausting[i][-1] ^= rightBitmask

        visited = [[False]*len(grid) for _ in range(len(grid))]
        active = {(0, 0)}

        # dijkstra-like approach
        t = max(grid[0][0], grid[-1][-1])
        nextT = max(t, min(grid[1][0], grid[0][1]))
        levelNeighbors = defaultdict(set)
        levelNeighbors[nextT].add((0,0))
        neiHeap = [nextT]

        while (len(grid) - 1, len(grid) - 1) not in active:
            t = nextT # O(max(grid) - max(grid[0][0], grid[-1][-1]))
            print(f't: {t}')
            print(f'active: {active}')
            nextT = heapq.heappop(neiHeap)
            newNodes = levelNeighbors[t]
            print(t, newNodes)
            while newNodes: # Each node can be added and WILL be added to newNodes from inside the loop only once. O(n²)
                x, y = newNodes.pop()
                moves = exhausting[x][y] ^ exhaustedBitmask
                # UP
                if moves & upBitmask and not visited[x-1][y]:
                    if grid[x-1][y] <= t:
                        moves ^= upBitmask
                        visited[x-1][y] = True
                        active.add((x-1, y))
                        newNodes.add((x-1, y))
                    else:
                        levelNeighbors[grid[x-1][y]].add((x, y))
                        heapq.heappush(neiHeap, grid[x-1][y])

                # DOWN
                if moves & downBitmask and not visited[x+1][y]:
                    if grid[x+1][y] <= t:
                        moves ^= downBitmask
                        visited[x+1][y] = True
                        active.add((x+1, y))
                        newNodes.add((x+1, y))
                    else:
                        levelNeighbors[grid[x+1][y]].add((x, y))
                        heapq.heappush(neiHeap, grid[x+1][y])

                # LEFT
                if moves & leftBitmask and not visited[x][y-1]:
                    if grid[x][y-1] <= t:
                        moves ^= leftBitmask
                        visited[x][y-1] = True
                        active.add((x, y-1))
                        newNodes.add((x, y-1))
                    else:
                        levelNeighbors[grid[x][y-1]].add((x, y))
                        heapq.heappush(neiHeap, grid[x][y-1])

                # RIGHT
                if moves & rightBitmask and not visited[x][y+1]:
                    if grid[x][y+1] <= t:
                        moves ^= rightBitmask
                        visited[x][y+1] = True
                        active.add((x, y+1))
                        newNodes.add((x, y+1))
                    else:
                        levelNeighbors[grid[x][y+1]].add((x, y))
                        heapq.heappush(neiHeap, grid[x][y+1])

                if moves == 0:
                    active.discard((x, y))
        return t