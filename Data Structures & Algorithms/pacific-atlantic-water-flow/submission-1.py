class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Obviously the top-right and the bottom-left borders should always be in the answer
        # We must find other which water can flow into both oceans
        # Special cases:
        # 1xn or nx1, where all cells border both oceans:
        if len(heights) == 1 or len(heights[0]) == 1:
            res = []
            for i in range(len(heights)):
                for j in range(len(heights[0])):
                    res.append([i, j])
            return res

        # Now let's think on how they act, starting by a small example
        # 2x2
        # if [0][0] is higher then either [0][1] or [1][0] then it should be in the answer
        # Similarly for [1][1]

        # We may draw the paths it can go, like a graph, then, we can dfs from each peak to find all solutions
        # Or pehaps we can start by the borders and note on them if they can reach the specific ocean
        atlantic = set()
        pacific = set()

        def goUpwards(i, j, ocean):
            if (i, j) in ocean:
                return
            print(i, j)
            ocean.add((i, j))
            if i > 0 and heights[i - 1][j] >= heights[i][j]:
                goUpwards(i - 1, j, ocean)
            if i < len(heights) - 1 and heights[i + 1][j] >= heights[i][j]:
                goUpwards(i + 1, j, ocean)
            if j > 0 and heights[i][j - 1] >= heights[i][j]:
                goUpwards(i, j - 1, ocean)
            if j < len(heights[0]) - 1 and heights[i][j + 1] >= heights[i][j]:
                goUpwards(i, j + 1, ocean)

        
        for i in range(len(heights)):
            #[i][0] for pacific
            print('left', i)
            goUpwards(i, 0, pacific)
            #[i][-1] for atlantic
            print('right')
            goUpwards(i, len(heights[0]) - 1, atlantic)
        for i in range(len(heights[0])):
            #[0][i] for pacific
            print('top', i)
            goUpwards(0, i, pacific)
            #[-1][i] for atlantic
            print('bottom')
            goUpwards(len(heights) - 1, i, atlantic)
        return [list(x) for x in (atlantic & pacific)]
        
