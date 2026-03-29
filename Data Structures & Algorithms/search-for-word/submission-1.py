class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def testPosition(i, j, k, visited):
            if k >= len(word):
                return True
            if j + 1 < len(board[0]) and (i, j + 1) not in visited and board[i][j + 1] == word[k]:
                visited.add((i, j+1))
                if testPosition(i, j + 1, k + 1, visited):
                    return True
                visited.discard((i, j+1))

            if j - 1 >= 0 and (i, j - 1) not in visited and board[i][j - 1] == word[k]:
                visited.add((i, j - 1))
                if testPosition(i, j - 1, k + 1, visited):
                    return True
                visited.discard((i, j - 1))

            if i + 1 < len(board) and (i + 1, j) not in visited and board[i + 1][j] == word[k]:
                visited.add((i + 1, j))
                if testPosition(i + 1, j, k + 1, visited):
                    return True
                visited.discard((i + 1, j))

            if i - 1 >= 0 and (i - 1, j) not in visited and board[i - 1][j] == word[k]:
                visited.add((i - 1, j))
                if testPosition(i - 1, j, k + 1, visited):
                    return True
                visited.discard((i - 1, j))

            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and testPosition(i, j, 1, {(i, j)}):
                        return True

        return False