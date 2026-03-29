class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def protect(i, j):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != 'O':
                # print('rejected', i, j)
                return
            # print(i, j)
            board[i][j] = '_'
            protect(i - 1, j)
            protect(i + 1, j)
            protect(i, j - 1)
            protect(i, j + 1)

        # First we protect the groups that cannot be surrounded
        for i in range(len(board)):
            protect(i,0)
            protect(i,len(board[0])-1)
        for j in range(len(board[0])):
            protect(0, j)
            protect(len(board) - 1, j)
        
        # print(board)
        # Then we swap ALL others
        for i in range(1, len(board) - 1):
            for j in range(1, len(board[0]) - 1):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        # print(board)

        # Then we revert the protected cells
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '_':
                    board[i][j] = 'O'
