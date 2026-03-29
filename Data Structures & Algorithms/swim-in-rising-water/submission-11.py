class DSU:
    def __init__(self, size):
        self.__size = size
        self.__sizes = [0]*(size*size)
        self.__parents = [i for i in range(len(self.__sizes))]
    
    def index(self, i, j = None):
        if j is None:
            return self.__size*i[0] + i[1]
        return self.__size*i + j

    def parent(self, i, j = None):
        if j is not None:
            i = self.index(i, j)
        if isinstance(i, list) or isinstance(i, tuple):
            i = self.index(i)
        if self.__parents[i] == i:
            return i
        self.__parents[i] = self.parent(self.__parents[i])
        return self.__parents[i]

    def activate(self, i, j) -> None:
        index = self.index(i, j)
        self.__sizes[index] = 1
        if i > 0 and self.size(i-1, j) > 0:
            self.union((i, j), (i-1, j))
        if j > 0 and self.size(i, j-1) > 0:
            self.union((i, j), (i, j-1))
        if i < self.__size - 1 and self.size(i+1, j) > 0:
            self.union((i, j), (i+1, j))
        if j < self.__size - 1 and self.size(i, j+1) > 0:
            self.union((i, j), (i, j+1))

    def size(self, i, j):
        parent = self.parent(i, j)
        return self.__sizes[parent]

    def connected(self, a, b):
        return self.parent(a[0], a[1]) == self.parent(b[0], b[1])

    def union(self, a, b):
        if self.connected(a, b):
            return
        aIndex = self.index(a)
        bIndex = self.index(a)
        parentA = self.parent(a)
        parentB = self.parent(b)
        if self.__sizes[parentA] < self.__sizes[parentB]:
            self.__parents[parentA] = parentB
            self.__sizes[parentB] += self.__sizes[parentA]
        else:
            self.__parents[parentB] = parentA
            self.__sizes[parentA] += self.__sizes[parentB]

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Kruskal-style
        n = len(grid)
        heap = [(grid[i][j], i, j) for i in range(n) for j in range(n)]
        heapq.heapify(heap)
        dsu = DSU(n)
        t = 0
        while not dsu.connected((0, 0), (n-1, n-1)):
            t, i, j = heapq.heappop(heap)
            dsu.activate(i, j)
        return t