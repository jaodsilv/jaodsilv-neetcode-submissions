import heapq

class DSU:
    def __init__(self, size):
        self.parents = [i for i in range(size*size)]
        self.sizes = [0 for _ in range(size*size)]
    
    def getParent(self, i):
        if self.parents[i] == i:
            return i
        self.parents[i] = self.getParent(self.parents[i])
        return self.parents[i]

    def union(self, i, j):
        parentI = self.getParent(i)
        parentJ = self.getParent(j)
        if parentI == parentJ:
            return False
        if self.sizes[parentI] > self.sizes[parentJ]:
            self.sizes[parentI] += self.sizes[parentJ]
            self.parents[parentJ] = parentI
        else:
            self.sizes[parentJ] += self.sizes[parentI]
            self.parents[parentI] = parentJ
        return True

    def connected(self, i, j):
        return self.getParent(i) == self.getParent(j)

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        def isValid(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid)

        def solutionBinarySearch():

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

        def solutionDijkstra():
            minT = max(grid[0][0], grid[-1][-1])
            heap = [(minT, 0, 0)]
            visited = set()
            while heap:
                nextT, i, j = heapq.heappop(heap)
                if i == j == len(grid) - 1:
                    return nextT
                if (i, j) in visited:
                    continue
                visited.add((i, j))

                if isValid(i-1, j) and (i-1, j) not in visited:
                    heapq.heappush(heap, (max(nextT, grid[i-1][j]), i-1, j))
                if isValid(i+1, j) and (i+1, j) not in visited:
                    heapq.heappush(heap, (max(nextT, grid[i+1][j]), i+1, j))
                if isValid(i, j-1) and (i, j-1) not in visited:
                    heapq.heappush(heap, (max(nextT, grid[i][j-1]), i, j-1))
                if isValid(i, j+1) and (i, j+1) not in visited:
                    heapq.heappush(heap, (max(nextT, grid[i][j+1]), i, j+1))
            return minT

        def isOpen(i, j, t):
            return  isValid(i, j) and grid[i][j] <= t

        def solutionKruskal():
            # baseT = max(grid[0][0], grid[-1][-1])
            allCells = [(grid[i][j], i, j) for i in range(len(grid)) for j in range(len(grid))]
            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

            allCells.sort(key=lambda x: x[0])
            dsu = DSU(len(grid))
            for t, i, j in allCells:
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if isOpen(ni, nj, t):
                        dsu.union(i*len(grid) + j, ni * len(grid) + nj)
                    if dsu.connected(0, len(grid)**2 - 1):
                        return t
            return 0

        # return solutionBinarySearch()
        # return solutionDijkstra()
        return solutionKruskal()