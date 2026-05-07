'''
Wrap the board in a 'O' margin
Create a Union-Find class
Add all cells in the union-find tree
Then loop all O cells. If it is in the same group as (-1,-1) of the (border), then we keep as is,
Otherwise we change to X
'''

class UF:
    def __init__(self, H, W) -> None:
        self.W = W+2
        self.parents = [i for i in range(self.W*(H+2))]
        self.sizes = [1]*(self.W*(H+2))
        print(W, H, len(self.parents), len(self.sizes))

    def _index(self, i: int, j: int) -> int:
        return (i+1)*self.W + j + 1

    def find(self, i: int, j: int) -> int:
        return self._find(self._index(i, j))

    def _find(self, i: int) -> int:
        p = self.parents[i]
        if i == p:
            return p
        self.parents[i] = self._find(p)
        return self.parents[i]

    def union(self, i1: int, j1: int, i2: int, j2: int) -> bool:
        p1 = self.find(i1, j1)
        p2 = self.find(i2, j2)
        if p1 == p2:
            return True
        if p1 == 0 or self.sizes[p1] >= self.sizes[p2]:
            self.parents[p2] = p1
            self.sizes[p1] += self.sizes[p2]
        else:
            self.parents[p1] = p2
            self.sizes[p2] += self.sizes[p1]
        return False
    def isConnectedToBorder(self, i, j):
        return self.find(i, j) == 0

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        uf = UF(m, n)
        for i in range(m+1):
            uf.union(-1, -1, i, -1)
            uf.union(-1, -1, i, n)

        for i in range(n+1):
            uf.union(-1, -1, -1, i)
            uf.union(-1, -1, m, i)

        for i, r in enumerate(board):
            for j, v in enumerate(r):
                if v == 'O':
                    if i == 0 or board[i-1][j] == 'O':
                        uf.union(i-1, j, i, j)
                    if j == 0 or board[i][j-1] == 'O':
                        uf.union(i, j-1, i, j)
                    if i == m-1 or board[i+1][j] == 'O':
                        uf.union(i+1, j, i, j)
                    if j == n-1 or board[i][j+1] == 'O':
                        uf.union(i, j+1, i, j)

        for i in range(m):
            for j in range(n):
                if not uf.isConnectedToBorder(i, j):
                    board[i][j] = 'X'
