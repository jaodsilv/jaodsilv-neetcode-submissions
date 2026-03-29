import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        def isValid(i, j):
            return i >= 0 and j >= 0 and i < len(grid) and j < len(grid)
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

        # return solutionBinarySearch()
        return solutionDijkstra()