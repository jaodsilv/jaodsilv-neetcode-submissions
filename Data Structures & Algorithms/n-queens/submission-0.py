class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [['Q']]

        def canAttackDiagonal(i, j, queen):
            return abs(i-queen[0]) == abs(j-queen[1])
        
        def buildBoard(queens):
            board = []
            for i in range(n):
                s = []
                for j in range(n):
                    if (i, j) in queens:
                        s.append('Q')
                    else:
                        s.append('.')
                board.append(''.join(s))
            return board

        # board = []
        # for i in range(n):
            # board.append(['.']*n)
        
        res = []

        def backtracking(j, queens, rows):
            print(j, queens, rows)
            if j == n:
                res.append(buildBoard(queens))
                return

            for i in rows.copy():
                hasConflict = False
                for queen in queens:
                    if canAttackDiagonal(i, j, queen):
                        hasConflict = True
                        break
                if not hasConflict:
                    rows.discard(i)
                    queens.add((i, j))
                    backtracking(j + 1, queens, rows)
                    queens.discard((i, j))
                    rows.add(i)

        backtracking(0, set(), set(range(n)))

        return res
