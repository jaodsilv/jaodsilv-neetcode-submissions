# class UF:
#     def __init__(self, H, W) -> None:
#         self.W = W + 2
#         self.H = H + 2
#         self.size = self.W*self.H
#         self._sizes = [1]*self.size
#         self._parents = [i for i in range(self.size)]
#     def _index(self, i: int, j: int) -> int:
#         return self.W*(i+1) + j + 1

#     def find(self, i: int, j: int) -> int:
#         index = self._index(i, j)
#         # if index >= len(self._parents):
#         #     print(i, j, index, len(self._parents), self.W, self.H)
#         return self._find(index)

#     def _find(self, i: int) -> int:
#         if self._parents[i] == i:
#             return i
#         self._parents[i] = self._find(self._parents[i])
#         return self._parents[i]

#     def union(self, i1: int, j1: int, i2: int, j2: int) -> bool:
#         # if i1 == 5 or i2 == 5:
#         #     print(i1, j1, i2, j2)
#         p1 = self.find(i1, j1)
#         p2 = self.find(i2, j2)
#         if p1 == p2:
#             return False
#         if self._sizes[p1] >= self._sizes[p2]:
#             self._parents[p2] = p1
#             self._sizes[p1] += self._sizes[p2]
#         else:
#             self._parents[p1] = p2
#             self._sizes[p2] += self._sizes[p1]

#         return True

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # We must find all 'O' groups that do not connect to the borders
        # Let's use a UnionFind to find the connected ones
        # To make it easier, let's imagine the board by 'O', which means the side is actually +2 to each side and the indexes will be shifted by 1
        # H = len(board)
        # W = len(board[0])
        # uf = UF(H, W)
        # for i in range(-1, H):
        #     uf.union(i, -1, i, W)
        #     uf.union(i, -1, i+1, -1)
        #     uf.union(i, W, i+1, W)
        # uf.union(H, -1, H, W)

        # for j in range(-1, W):
        #     uf.union(-1, j, H, j)
        #     uf.union(-1, j, -1, j+1)
        #     uf.union(H, j, H, j+1)
        # # uf.union(-1, W, H, W)


        # # for i in range(-1, H+1):
        # #     print([uf.find(i, j) for j in range(-1, W+1)])

        # # print()
        # for i, r in enumerate(board):
        #     for j, v in enumerate(r):
        #         if v == 'O':
        #             if i == 0 or board[i-1][j] == 'O':
        #                 uf.union(i, j, i-1, j)
        #             if j == 0 or board[i][j-1] == 'O':
        #                 uf.union(i, j, i, j-1)
        #             if i == H-1 or board[i+1][j] == 'O':
        #                 uf.union(i, j, i+1, j)
        #             if j == W-1 or board[i][j+1] == 'O':
        #                 uf.union(i, j, i, j+1)
        # # for i in range(-1, H+1):
        # #     print([uf.find(i, j) for j in range(-1, W+1)])
        # border = uf.find(-1,-1)
        # for i, r in enumerate(board):
        #     for j, v in enumerate(r):
        #         if v == 'O' and uf.find(i, j) != border:
        #             board[i][j] = 'X'
        # # print(board)

        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != 'O':
                return
            board[i][j] = 'T'
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        for i in range(len(board)):
            dfs(i, 0)
            dfs(i, len(board[0])-1)
        for j in range(len(board[0])):
            dfs(0, j)
            dfs(len(board)-1, j)
        # print(visited)
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = 'O' if board[i][j] == 'T' else 'X'
