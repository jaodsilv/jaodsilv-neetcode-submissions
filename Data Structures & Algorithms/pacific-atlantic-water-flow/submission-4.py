class Node:
    def __init__(self) -> None:
        self.neis = set()

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        nodes = {}
        if len(heights) == 1 or len(heights[0]) == 1:
            res = []
            for i in range(len(heights)):
                for j in range(len(heights[0])):
                    res.append([i, j])
            return res

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                node = None
                if (i, j) in nodes:
                    node = nodes[(i, j)]
                else:
                    node = set()
                    nodes[(i, j)] = node
                h = heights[i][j]

        # DP = [[1]*(len(heights[0]) - 1) + [3]]
        # DP.extend([[1] + [0]*(len(heights[0])-2) + [2] for _ in range(len(heights) - 2)])
        # DP.append([3] + [2]*(len(heights[0]) - 1))
        visited = set()
        def dfs(i, j, ocean):
            ij = (i, j)
            if ij in ocean:
                return
            ocean.add(ij)
            h = heights[i][j]
            if i > 0 and heights[i-1][j] >= h:
                dfs(i-1, j, ocean)
            if j > 0 and heights[i][j-1] >= h:
                dfs(i, j-1, ocean)
            if i < len(heights) - 1 and heights[i+1][j] >= h:
                dfs(i+1, j, ocean)
            if j < len(heights[0]) - 1 and heights[i][j+1] >= h:
                dfs(i, j+1, ocean)

        atlantic = set()
        pacific = set()

        for i in range(len(heights)):
            dfs(i, 0, pacific)
            dfs(i, len(heights[0]) - 1, atlantic)
        
        for i in range(len(heights[0])):
            dfs(0, i, pacific)
            dfs(len(heights) - 1, i, atlantic)


        res = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                ij = (i, j)
                if ij in atlantic and ij in pacific:
                    res.append([i, j])
        return res
