class UnionFindTree:
    def __init__(self, n: int):
        self.n = n
        self.parents = [i for i in range(n*n)]
        self.sizes = [1] * (n*n)

    def __index(self, i: int, j: int) -> int:
        return j + i*self.n

    def parent(self, i: int, j: int) -> int:
        return self.__parent(self.__index(i, j))

    def __parent(self, i: int) -> int:
        if self.parents[i] == i:
            return i
        self.parents[i] = self.__parent(self.parents[i])
        return self.parents[i]

    def union(self, ai: int, aj: int, bi: int, bj: int):
        pa = self.parent(ai, aj)
        pb = self.parent(bi, bj)
        if pa == pb:
            return
        
        if self.sizes[pa] > self.sizes[pb]:
            self.sizes[pa] += self.sizes[pb]
            self.parents[pb] = pa
        else:
            self.sizes[pb] += self.sizes[pa]
            self.parents[pa] = pb

    def connected(self, ai: int, aj: int, bi: int, bj: int) -> bool:
        return self.parent(ai, aj) == self.parent(bi, bj)

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        '''
        values are between 0 and 2500, which is also the number of elements in the matrix
        '''
        n = len(grid)
        values = [set() for _ in range(n*n)]

        for r in range(len(grid)):
            for c, v in enumerate(grid[r]):
                values[v].add((r, c))
        
        dst = UnionFindTree(n)
        for v, s in enumerate(values):
            for i, j in s:
                if i > 0 and v > grid[i-1][j]:
                    dst.union(i, j, i-1, j)
                if j > 0 and v > grid[i][j-1]:
                    dst.union(i, j, i, j-1)
                if i < n - 1 and v > grid[i+1][j]:
                    dst.union(i, j, i+1, j)
                if j < n - 1 and v > grid[i][j+1]:
                    dst.union(i, j, i, j+1)
            if dst.connected(0,0,n-1,n-1):
                return v
                




