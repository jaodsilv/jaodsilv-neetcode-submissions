import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        '''
        values are between 0 and 2500, which is also the number of elements in the matrix
        '''
        n = len(grid)

        neighbors = [(grid[0][0], 0,0)]
        visited=set()
        maxV = grid[0][0]
        for i in range(n):
            visited.add((-1, i))
            visited.add((n, i))
            visited.add((i, -1))
            visited.add((i, n))
        while True:
            v, i, j = heapq.heappop(neighbors)
            maxV = max(maxV, v)
            if i == n-1 and j == n-1:
                return maxV
            if (i+1, j) not in visited:
                visited.add((i+1, j))
                heapq.heappush(neighbors, (grid[i+1][j], i+1, j))
            if (i, j + 1) not in visited:
                visited.add((i, j+1))
                heapq.heappush(neighbors, (grid[i][j+1], i, j+1))
            if (i-1, j) not in visited:
                visited.add((i-1, j))
                heapq.heappush(neighbors, (grid[i-1][j], i-1, j))
            if (i, j-1) not in visited:
                visited.add((i, j-1))
                heapq.heappush(neighbors, (grid[i][j-1], i, j-1))
                




