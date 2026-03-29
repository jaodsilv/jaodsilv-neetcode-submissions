class Node:
    def __init__(self):
        self.children = {}
        self.index = None

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word, index):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.index = index

    def search(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.index is not None

    def startsWith(self, prefix):
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True

class Solution:
    def dfs(self, board, node, i, j, visited, found):
        visited.add((i,j))
        if i > 0 and (i-1, j) not in visited and board[i-1][j] in node.children:
            next = node.children[board[i-1][j]]
            index = next.index
            if index is not None:
                found[index] = True
            self.dfs(board, next, i-1, j, visited, found)
        if i < len(board) - 1 and (i+1, j) not in visited and board[i+1][j] in node.children:
            next = node.children[board[i+1][j]]
            index = next.index
            if index is not None:
                found[index] = True
            self.dfs(board, next, i+1, j, visited, found)
        if j > 0 and (i, j-1) not in visited and board[i][j-1] in node.children:
            next = node.children[board[i][j-1]]
            index = next.index
            if index is not None:
                found[index] = True
            self.dfs(board, next, i, j-1, visited, found)
        if j < len(board[0]) - 1 and (i, j+1) not in visited and board[i][j+1] in node.children:
            next = node.children[board[i][j+1]]
            index = next.index
            if index is not None:
                found[index] = True
            self.dfs(board, next, i, j+1, visited, found)
        visited.discard((i,j))

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for i in range(len(words)):
            word = words[i]
            trie.insert(word, i)

        found = [False]*len(words)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] not in trie.root.children:
                    continue
                next = trie.root.children[board[i][j]]
                if next.index is not None:
                    found[next.index] = True
                self.dfs(board, next, i, j, set(), found)

        return [word for word, present in zip(words, found) if present]