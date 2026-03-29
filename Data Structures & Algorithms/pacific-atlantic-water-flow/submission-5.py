class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        hs = defaultdict(list)
        values = set()
        pacific = set()
        atlantic = set()

        def dfs(r, c, ocean):
            if (r, c) in ocean:
                return True
            ocean.add((r, c))
            h = heights[r][c]
            if r > 0 and heights[r-1][c] >= h:
                dfs(r-1, c, ocean)
            if c > 0 and heights[r][c-1] >= h:
                dfs(r, c-1, ocean)
            if r < len(heights)-1 and heights[r+1][c] >= h:
                dfs(r+1, c, ocean)
            if c < len(heights[0])-1 and heights[r][c+1] >= h:
                dfs(r, c+1, ocean)
        
        for j in range(len(heights[0])):
            dfs(0, j, pacific)
            dfs(len(heights)-1, j, atlantic)

        for i in range(len(heights)):
            dfs(i, 0, pacific)
            dfs(i, len(heights[0])-1, atlantic)
        
        return [list(a) for a in atlantic&pacific]
        
        