class Solution:
    def dfs(self, board, word, visited, pos) -> bool:
        visited.add(pos)
        if len(word) == 0:
            return True

        char = word.pop()
        neighbor = (pos[0], pos[1] + 1)
        if pos[1] + 1 < len(board[0]) and neighbor not in visited and board[neighbor[0]][neighbor[1]] == char and self.dfs(board, word, visited, neighbor):
                return True

        neighbor = (pos[0], pos[1] - 1)
        if pos[1] - 1 >= 0 and neighbor not in visited and board[neighbor[0]][neighbor[1]] == char and self.dfs(board, word, visited, neighbor):
                return True

        neighbor = (pos[0] + 1, pos[1])
        if pos[0] + 1 < len(board) and neighbor not in visited and board[neighbor[0]][neighbor[1]] == char and self.dfs(board, word, visited, neighbor):
                return True

        neighbor = (pos[0] - 1, pos[1])
        if pos[0] - 1 >= 0 and neighbor not in visited and board[neighbor[0]][neighbor[1]] == char and self.dfs(board, word, visited, neighbor):
                return True

        word.append(char)
        visited.discard(pos)
        return False

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        output = []
        # Prepare board
        chars = [None]*(ord('z') - ord('a') + 1)
        for i in range(len(chars)):
            chars[i] = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                chars[ord(board[i][j]) - ord('a')].append((i,j))
        
        print(chars)
        for word in words:
            wordList = list(word)
            char = wordList.pop()
            inits = chars[ord(char) - ord('a')]
            for init in inits:
                if self.dfs(board, wordList, set(), init):
                    output.append(word)
                    break

        return output
