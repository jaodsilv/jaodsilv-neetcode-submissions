class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def testSquare(i, j):
            vals = set(range(1, 10))
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    if board[k][l] != ".":
                        if int(board[k][l]) in vals:
                            vals.discard(int(board[k][l]))
                        else:
                            return False
            return True
        def testRow(i):
            vals = set(range(1, 10))
            for k in range(9):
                if board[i][k] != ".":
                    if int(board[i][k]) in vals:
                        vals.discard(int(board[i][k]))
                    else:
                        return False
            return True
        def testCol(j):
            vals = set(range(1, 10))
            for k in range(9):
                if board[k][j] != ".":
                    if int(board[k][j]) in vals:
                        vals.discard(int(board[k][j]))
                    else:
                        return False
            return True

        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                if not testSquare(i, j):
                    return False
        for i in range(9):
            if not testRow(i):
                return False
            if not testCol(i):
                return False
        return True

