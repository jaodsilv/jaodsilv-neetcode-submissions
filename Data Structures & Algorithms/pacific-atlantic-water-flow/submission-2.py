class Node:
    def __init__(self, h, i, j):
        self.h = h
        self.i = i
        self.j = j
        self.pacific = i == 0 or j == 0
        self.atlantic = False
        self.nei = []
    

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def pacific(i, j) -> bool:
            return i == 0 or j == 0
        def atlantic(i, j) -> bool:
            return i == len(heights) - 1 or j == len(heights[0]) - 1

        memo = {}
        parents = [[(i,j) for j in range(len(heights[0]))] for i in range(len(heights))]
        sizes = [[1]*len(heights[0]) for _ in range(len(heights))]
        def parent(i, j):
            if parents[i][j] == (i, j):
                return (i, j)
            curr = parents[i][j]
            parents[i][j] = parent(curr[0], curr[1])
            return parents[i][j]

        def merge(a, b):
            parentA = parent(a[0], a[1])
            parentB = parent(b[0], b[1])
            if parentA == parentB:
                return
            sizeA = sizes[parentA[0]][parentA[1]]
            sizeB = sizes[parentB[0]][parentB[1]]
            if sizeA > sizeB:
                sizes[parentA[0]][parentA[1]] = sizeA + sizeB
                parents[parentB[0]][parentB[1]] = parentA
            else:
                sizes[parentB[0]][parentB[1]] = sizeA + sizeB
                parents[parentA[0]][parentA[1]] = parentB

        neis = []
        for i, r in enumerate(heights):
            neis.append([])
            for j, h in enumerate(r):
                neis[-1].append([])
                if i > 0:
                    if heights[i-1][j] < h:
                        neis[-1][-1].append((i-1, j))
                    elif heights[i-1][j] == h:
                        merge((i, j), (i-1, j))
                if j > 0:
                    if heights[i][j-1] < h:
                        neis[-1][-1].append((i, j-1))
                    elif heights[i][j-1] == h:
                        merge((i, j), (i, j-1))
                if i < len(heights) - 1:
                    if heights[i+1][j] < h:
                        neis[-1][-1].append((i+1, j))
                    elif heights[i+1][j] == h:
                        merge((i, j), (i+1, j))
                if j < len(heights[0]) - 1:
                    if heights[i][j+1] < h:
                        neis[-1][-1].append((i, j+1))
                    elif heights[i][j+1] == h:
                        merge((i, j), (i, j+1))

        siblings = {}
        for i in range(len(parents)):
            for j in range(len(parents[0])):
                p = parent(i, j)
                if p not in siblings:
                    siblings[p] = []
                siblings[p].append((i, j))
                
        def dfs(i, j) -> int:
            if i < 0 or j < 0 or i == len(heights) or j == len(heights[0]):
                return 0

            par = parent(i, j)
            if par in memo:
                return memo[par]

            sibs = siblings[par]
            res = 0

            neiList = []
            for sib in sibs:
                neiList.extend(neis[sib[0]][sib[1]])
                if atlantic(sib[0], sib[1]):
                    res |= 1
                if pacific(sib[0], sib[1]):
                    res |= 2
                if res == 3:
                    memo[par] = 3
                    return 3

            for k, l in neiList:
                res |= dfs(k, l)

            memo[par] = res
            return res
                
        resp = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if dfs(i, j) == 3:
                    resp.append((i, j))
        return resp