import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return 0
        infinity = max([max(r) for r in grid]) + 1
        tMin = max(grid[0][0], grid[-1][-1])
        # memo = {(n-1, n-1): (tMin, True)}
        # for i in range(len(grid)):
        #     memo[(-1, i)] = (infinity, False)
        #     memo[(n, i)] = (infinity, False)
        #     memo[(i, n)] = (infinity, False)
        #     memo[(i, -1)] = (infinity, False)
        # Representing the minimum level given we are already 
        # dp = [[infinity]*(len(grid)+1) for _ in range(len(grid) + 1)]
        # dp[-2][-2] = tMin
        # Min heap to get the next min
        heap = [(grid[-1][-1], n-1, n-1)]
        visited = set()
        # BFS
        cost = tMin
        while heap:
            cost, i, j = heapq.heappop(heap)
            if (i, j) in visited:
                continue
            print(cost, i, j, grid[i][j])
            visited.add((i, j))
            if i == 0 and j == 0:
                return cost
            
            # if dp[i][j] != infinity:
            #     return dp[i][j]

            if i < n -1:
                heapq.heappush(heap, (max(cost, grid[i+1][j]), i+1, j))
            if j < n - 1:
                heapq.heappush(heap, (max(cost, grid[i][j+1]), i, j + 1))
            if i > 0:
                heapq.heappush(heap, (max(cost, grid[i-1][j]), i-1, j))
            if j > 0:
                heapq.heappush(heap, (max(cost, grid[i][j-1]), i, j - 1))
        return cost
            # print(f'dfs({i}, {j})')

            # t = infinity
            # tNei = min(dfs(i, j - 1), dfs(i - 1, j))
            # t = min(t, tNei)
            # if valid:
            #     t = min(t, tNei)
            # tNei, valid = dfs(i, j - 1)
            # if valid:
            #     t = min(t, tNei)
            # tNei, valid = dfs(i - 1, j)
            # if valid:
            #     t = min(t, tNei)
            # t = max(grid[i][j], tNei)

            # memo[(i, j)] = (t, True)
            # print(f'memo[({i}, {j})] = ({t}, True)')
            # return memo[(i, j)]
        # return dfs(0, 0)[0]#n-1, n-1)

'''
[ 0, 1, 2,10]
[ 9,14, 4,13]
[12, 3, 8,15]
[11, 5, 7, 6]
'''